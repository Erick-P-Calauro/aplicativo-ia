import os
from pathlib import Path
from dotenv import load_dotenv

# Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
PHOTOS_DIR = DATA_DIR / "photos"
MODELS_DIR = DATA_DIR / "models"
DATA_DIR.mkdir(exist_ok=True)
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Raiz do projeto (configuration -> Src -> api -> projeto), independente da máquina
PROJECT_ROOT = BASE_DIR.parent
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=False)

# DB
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ROOT USER
ROOT_USER = os.getenv("ROOT_USER")
ROOT_PASSWD = os.getenv("ROOT_PASSWD")

# Auth
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = 60

# Reconhecimento Facial
THRESHOLD = 0.688
YUNET_MODEL_URL = os.getenv("YUNET_MODEL_URL")
YUNET_MODEL_NAME = os.getenv("YUNET_MODEL_NAME")
