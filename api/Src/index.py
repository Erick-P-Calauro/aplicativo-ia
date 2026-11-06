import os
import uuid

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .configuration.config import PHOTOS_DIR, ROOT_USER, ROOT_PASSWD
from .repository.connection import Base, engine, get_db
from .models import User, UserResponse, FaceBox, FaceResult, RecognitionResponse
from .models.dtos import (
    TokenResponse,
    LoginRequest,
    RecognitionEmptyResponse,
)
from .configuration.auth import create_access_token, verify_token, authenticate_root
from .logger import logger
from .service.face_service import (
    generate_embedding,
    recognize_faces,
    serialize_vector,
    deserialize_vector,
)
from .repository import user_repository, embedding_repository

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aplicativo Reconhecimento Facial")


@app.on_event("startup")
def on_startup():
    logger.info("Servidor iniciado")


def _save_photo(user_id: uuid.UUID, data: bytes, filename: str) -> str:
    ext = os.path.splitext(filename)[1] or ".jpg"
    path = PHOTOS_DIR / f"{user_id}{ext}"
    with open(path, "wb") as f:
        f.write(data)
    return str(path)


@app.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    if not authenticate_root(payload.root_user, payload.root_passwd):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = create_access_token(ROOT_USER)
    return TokenResponse(access_token=token)


@app.get("/user", response_model=list[UserResponse])
def listar_users(db: Session = Depends(get_db), _=Depends(verify_token)):
    return user_repository.list_users(db)


@app.post("/user/cadastrar", response_model=UserResponse, status_code=201)
async def cadastrar_user(
    name: str = Form(...),
    photo: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not photo.content_type or not photo.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado")
    data = await photo.read()
    if not data:
        raise HTTPException(status_code=400, detail="Foto ausente")

    user_id = uuid.uuid4()
    photo_path = _save_photo(user_id, data, photo.filename or "photo.jpg")

    try:
        vec, _ = generate_embedding(data)
    except ValueError as e:
        try:
            os.remove(photo_path)
        except OSError:
            pass
        raise HTTPException(status_code=422, detail=str(e))

    user = User(id=user_id, name=name, photo_path=photo_path)
    user_repository.create_user(db, user)
    embedding_repository.create_embedding(db, user.id, serialize_vector(vec))

    logger.info(f"Usuário cadastrado id={user.id} name={user.name}")
    return user


@app.delete("/user/{user_id}", status_code=204)
def deletar_user(user_id: uuid.UUID, db: Session = Depends(get_db), _=Depends(verify_token)):
    user = user_repository.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    photo_path = user.photo_path
    user_repository.delete_user(db, user)
    logger.info(f"Usuário deletado id={user_id}")
    try:
        if photo_path and os.path.exists(photo_path):
            os.remove(photo_path)
    except OSError:
        pass
    return Response(status_code=204)


@app.post("/face/reconhecer")
async def reconhecer_face(
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado")
    data = await image.read()
    if not data:
        raise HTTPException(status_code=400, detail="Imagem inválida")

    known_raw = embedding_repository.get_all_known(db)
    known = []
    for uid, name, vec_bytes in known_raw:
        known.append((uid, name, deserialize_vector(vec_bytes)))

    try:
        results, has_faces = recognize_faces(data, known)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not has_faces:
        logger.info("Nenhuma face encontrada na imagem")
        return {"message": "Nenhuma pessoa encontrada na imagem"}

    logger.info(f"{len(results)} face(s) reconhecida(s)")
    faces = []
    for box, name, uid, score in results:
        x, y, w, h = box
        faces.append(
            FaceResult(
                box=FaceBox(x=x, y=y, w=w, h=h),
                name=name,
                user_id=uid,
                score=score,
            )
        )
    return RecognitionResponse(faces=faces)
