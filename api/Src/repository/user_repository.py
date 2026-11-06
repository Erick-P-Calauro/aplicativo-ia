from sqlalchemy.orm import Session

from ..models.user import User


def list_users(db: Session):
    return db.query(User).order_by(User.created_at.desc()).all()


def get_user(db: Session, user_id):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
