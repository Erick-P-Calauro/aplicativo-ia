from sqlalchemy.orm import Session

from ..models.entities import Embedding


def create_embedding(db: Session, user_id, vector_bytes: bytes):
    emb = Embedding(user_id=user_id, vector=vector_bytes)
    db.add(emb)
    db.commit()
    return emb


def list_embeddings_for_user(db: Session, user_id):
    return db.query(Embedding).filter(Embedding.user_id == user_id).all()


def get_all_known(db: Session):
    """Retorna lista de (user_id, name, vector_bytes) para todos os usuários."""
    from ..models.entities import User

    result = []
    users = db.query(User).all()
    for u in users:
        for e in u.embeddings:
            result.append((u.id, u.name, e.vector))
    return result
