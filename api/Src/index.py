from fastapi import FastAPI
from fastapi import Response

app = FastAPI()

@app.get("/user")
async def listar_users():
    return Response("Usuários", status_code=200)

@app.post("/user/cadastrar")
async def cadastrar_user():
    return Response("Cadastrado", status_code=201)

# Deleta o usuário, sua imagem e o embedding associado
@app.delete("/user/{user_id}")
async def deletar_face(user_id):
    return Response("Deletado", status_code=204)

# Recebe imagem, detecta faces e reconhece cada face detectada
@app.post("/face/reconhecer")
async def reconhecer_face():
    return Response("Reconhecido", status_code=200)