import csv
import os
import uuid

from src.backend.project_service import get_all_projects, PROJECTS_FILE
from src.crypto.signature_utils import create_signature, verify_signature
from src.crypto.hmac_utils import create_hmac, verify_hmac
from src.backend.student_service import get_student_by_id

ENROLLMENTS_FILE = "data/enrollments.csv"
HEADERS = [
    "enrollment_id",
    "student_id",
    "student_name",
    "student_email",
    "project_id",
    "project_name",
    "message",
    "signature",
    "record_hmac",
]


def initialize_enrollments_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(ENROLLMENTS_FILE) or os.path.getsize(ENROLLMENTS_FILE) == 0:
        with open(ENROLLMENTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def get_all_enrollments():
    initialize_enrollments_file()

    with open(ENROLLMENTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def student_is_enrolled(student_id: str) -> bool:
    enrollments = get_all_enrollments()

    for enrollment in enrollments:
        if enrollment["student_id"] == student_id:
            return True

    return False


def get_enrollments_by_project(project_id: str):
    enrollments = get_all_enrollments()

    return [
        enrollment
        for enrollment in enrollments
        if enrollment["project_id"] == project_id
    ]


def enroll_student(student: dict, project_id: str):
    initialize_enrollments_file()

    if student_is_enrolled(student["student_id"]):
        return False, "Ya estás inscrito en un proyecto. No puedes inscribirte en otro."

    projects = get_all_projects()
    selected_project = None

    for project in projects:
        if project["project_id"] == project_id:
            selected_project = project
            break

    if selected_project is None:
        return False, "El proyecto no existe."

    available_slots = int(selected_project["available_slots"])

    if available_slots <= 0:
        return False, "Este proyecto ya está lleno."

    enrollment_id = str(uuid.uuid4())

    message_to_sign = (
        f"{student['student_id']}|"
        f"{selected_project['project_id']}|"
        f"{selected_project['name']}"
    )

    signature = create_signature(student["student_id"], message_to_sign)

    record_message = (
        f"{enrollment_id}|"
        f"{student['student_id']}|"
        f"{student['email']}|"
        f"{selected_project['project_id']}|"
        f"{selected_project['name']}|"
        f"{signature}"
    )

    record_hmac = create_hmac(record_message)

    with open(ENROLLMENTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                enrollment_id,
                student["student_id"],
                student["name"],
                student["email"],
                selected_project["project_id"],
                selected_project["name"],
                message_to_sign,
                signature,
                record_hmac,
            ]
        )

    selected_project["available_slots"] = str(available_slots - 1)

    with open(PROJECTS_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["project_id", "name", "capacity", "available_slots"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(projects)

    return True, "Inscripción realizada correctamente."


def verify_enrollment_hmac(enrollment: dict) -> bool:
    record_message = (
        f"{enrollment['enrollment_id']}|"
        f"{enrollment['student_id']}|"
        f"{enrollment['student_email']}|"
        f"{enrollment['project_id']}|"
        f"{enrollment['project_name']}|"
        f"{enrollment['signature']}"
    )

    return verify_hmac(record_message, enrollment["record_hmac"])


def verify_enrollment_signature(enrollment: dict) -> bool:
    student = get_student_by_id(enrollment["student_id"])

    if student is None:
        return False

    public_key = student.get("public_key")

    if not public_key:
        return False

    return verify_signature(public_key, enrollment["message"], enrollment["signature"])
