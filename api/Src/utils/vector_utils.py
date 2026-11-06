import numpy as np


def serialize_vector(vec: np.ndarray) -> bytes:
    return vec.astype("float32").tobytes()


def deserialize_vector(data: bytes) -> np.ndarray:
    return np.frombuffer(data, dtype=np.float32)
