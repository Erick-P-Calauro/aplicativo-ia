import cv2
import os
import numpy as np
from pathlib import Path

from ..configuration.config import PHOTOS_DIR


def save_photo(user_id, data: bytes, filename: str) -> str:
    ext = os.path.splitext(filename)[1] or ".jpg"
    path = PHOTOS_DIR / f"{user_id}{ext}"
    with open(path, "wb") as f:
        f.write(data)
    return str(path)


def read_image(image_bytes: bytes):
    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Imagem inválida ou não suportada")
    return img


def crop_image(img: np.ndarray, box):
    """Recorta uma região (x, y, w, h) de uma imagem."""
    x, y, w, h = box
    h_img, w_img = img.shape[:2]
    x = max(0, min(x, w_img - 1))
    y = max(0, min(y, h_img - 1))
    w = max(1, min(w, w_img - x))
    h = max(1, min(h, h_img - y))
    return img[y : y + h, x : x + w]
