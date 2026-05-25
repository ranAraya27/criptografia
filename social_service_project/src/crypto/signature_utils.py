import os
import base64

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives import serialization

KEYS_DIR = "data/keys/students"


def ensure_keys_dir():
    os.makedirs(KEYS_DIR, exist_ok=True)


def get_private_key_path(student_id: str) -> str:
    ensure_keys_dir()
    return f"{KEYS_DIR}/{student_id}_private.pem"


def generate_student_keys(student_id: str) -> str:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    with open(get_private_key_path(student_id), "wb") as file:
        file.write(private_bytes)

    return public_bytes.decode("utf-8")


def load_private_key(student_id: str):
    with open(get_private_key_path(student_id), "rb") as file:
        return serialization.load_pem_private_key(file.read(), password=None)


def load_public_key(public_key_pem: str):
    return serialization.load_pem_public_key(public_key_pem.encode("utf-8"))


def create_signature(student_id: str, message: str) -> str:
    private_key = load_private_key(student_id)
    signature = private_key.sign(message.encode("utf-8"))
    return base64.b64encode(signature).decode("utf-8")


def verify_signature(public_key_pem: str, message: str, signature_b64: str) -> bool:
    try:
        public_key = load_public_key(public_key_pem)
        signature = base64.b64decode(signature_b64.encode("utf-8"))

        public_key.verify(signature, message.encode("utf-8"))
        return True
    except Exception:
        return False
