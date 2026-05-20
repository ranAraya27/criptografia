import csv
import os
import uuid

from src.crypto.password_utils import hash_password, verify_password

STUDENTS_FILE = "data/students.csv"


def initialize_students_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["student_id", "name", "email", "password_hash"])


def email_exists(email: str) -> bool:
    initialize_students_file()

    with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["email"] == email:
                return True

    return False


def register_student(name: str, email: str, password: str) -> bool:
    initialize_students_file()

    if email_exists(email):
        return False

    student_id = str(uuid.uuid4())
    password_hash = hash_password(password)

    with open(STUDENTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, email, password_hash])

    return True


def login_student(email: str, password: str):
    initialize_students_file()

    with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["email"] == email:
                if verify_password(password, row["password_hash"]):
                    return row

    return None
