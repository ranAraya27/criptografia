import csv
import os
import uuid

from src.backend.project_service import get_all_projects, PROJECTS_FILE

ENROLLMENTS_FILE = "data/enrollments.csv"
HEADERS = [
    "enrollment_id",
    "student_id",
    "student_name",
    "student_email",
    "project_id",
    "project_name",
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
            ]
        )

    selected_project["available_slots"] = str(available_slots - 1)

    with open(PROJECTS_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["project_id", "name", "capacity", "available_slots"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(projects)

    return True, "Inscripción realizada correctamente."
