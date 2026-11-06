import io
import urllib.request
from pathlib import Path

import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import InceptionResnetV1

from ..utils.image_utils import read_image, crop_image
from ..utils.vector_utils import serialize_vector, deserialize_vector
from ..configuration.config import (
    MODELS_DIR,
    YUNET_MODEL_URL,
    YUNET_MODEL_NAME,
    THRESHOLD,
)

# --- YuNet model download -----------------------------------------------------
YUNET_PATH = MODELS_DIR / YUNET_MODEL_NAME
if not YUNET_PATH.exists():
    try:
        urllib.request.urlretrieve(YUNET_MODEL_URL, YUNET_PATH)
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"Falha ao baixar modelo YuNet: {exc}")

# --- Facenet (InceptionResnetV1) ---------------------------------------------
_DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_RESNET = InceptionResnetV1(pretrained="vggface2").eval().to(_DEVICE)

def detect_faces(image_bytes: bytes):
    """Retorna lista de (x, y, w, h) detectados com YuNet."""
    img = read_image(image_bytes)
    h, w = img.shape[:2]
    detector = cv2.FaceDetectorYN_create(
        str(YUNET_PATH), "", (w, h), 0.6, 0.3, 5000
    )
    _, faces = detector.detect(img)
    boxes = []
    if faces is not None:
        for f in faces:
            x, y, bw, bh = [int(v) for v in f[:4]]
            # clamp
            x = max(0, x)
            y = max(0, y)
            bw = max(1, min(bw, w - x))
            bh = max(1, min(bh, h - y))
            boxes.append((x, y, bw, bh))
    return img, boxes


def _crop_and_embed(img, box):
    x, y, w, h = box
    face = crop_image(img, (x, y, w, h))
    if face.size == 0:
        return None
    face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    pil = Image.fromarray(face_rgb).resize((160, 160))
    arr = np.asarray(pil).astype(np.float32)
    arr = (arr - 127.5) / 128.0
    tensor = torch.from_numpy(arr).permute(2, 0, 1).unsqueeze(0).to(_DEVICE)
    with torch.no_grad():
        emb = _RESNET(tensor)
    vec = emb.cpu().numpy().flatten().astype(np.float32)
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec


def generate_embedding(image_bytes: bytes):
    """Gera um embedding a partir da primeira face detectada na imagem.

    Retorna (vector np.ndarray float32, box). Levanta ValueError se nenhuma face.
    """
    img, boxes = detect_faces(image_bytes)
    if not boxes:
        raise ValueError("Nenhuma face detectada na imagem")
    # escolhe a maior face
    boxes_sorted = sorted(boxes, key=lambda b: b[2] * b[3], reverse=True)
    vec = _crop_and_embed(img, boxes_sorted[0])
    if vec is None:
        raise ValueError("Falha ao gerar embedding")
    return vec, boxes_sorted[0]


def recognize_faces(image_bytes: bytes, known: list):
    """known: list of (user_id, name, np.ndarray).

    Retorna (list of (box, name, user_id or None, score), has_faces).
    """
    img, boxes = detect_faces(image_bytes)
    if not boxes:
        return [], False

    results = []
    for box in boxes:
        vec = _crop_and_embed(img, box)
        if vec is None:
            continue
        best_uid = None
        best_name = "Não cadastrado"
        best_score = 0.0
        for (uid, name, kvec) in known:
            score = float(np.dot(vec, kvec))
            if score > best_score:
                best_score = score
                if score >= THRESHOLD:
                    best_uid = uid
                    best_name = name
        # if best below threshold, ensure not cadastrado
        if best_score < THRESHOLD:
            best_uid = None
            best_name = "Não cadastrado"
        results.append((box, best_name, best_uid, float(best_score)))
    return results, True


# serialize_vector / deserialize_vector moved to utils.vector_utils
