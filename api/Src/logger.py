import logging
from pathlib import Path

from .configuration.config import DATA_DIR

LOG_FILE = DATA_DIR / "app.log"

logger = logging.getLogger("aplicativo_ia")
logger.setLevel(logging.INFO)

if not logger.handlers:
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)
