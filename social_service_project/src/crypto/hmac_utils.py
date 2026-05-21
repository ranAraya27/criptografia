import os
import hmac
import hashlib
import base64

HMAC_KEY_FILE = "data/keys/hmac_secret.key"


def initialize_hmac_key():
    os.makedirs("data/keys", exist_ok=True)

    if not os.path.exists(HMAC_KEY_FILE):
        key = os.urandom(32)

        with open(HMAC_KEY_FILE, "wb") as file:
            file.write(key)


def load_hmac_key() -> bytes:
    initialize_hmac_key()

    with open(HMAC_KEY_FILE, "rb") as file:
        return file.read()


def create_hmac(message: str) -> str:
    key = load_hmac_key()

    mac = hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()

    return base64.b64encode(mac).decode("utf-8")


def verify_hmac(message: str, received_hmac: str) -> bool:
    expected_hmac = create_hmac(message)

    return hmac.compare_digest(expected_hmac, received_hmac)
