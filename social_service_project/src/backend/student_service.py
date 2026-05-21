import csv
from src.backend.auth_service import STUDENTS_FILE, initialize_students_file


def get_all_students():
    initialize_students_file()

    with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students = []

        for row in reader:
            students.append(
                {
                    "student_id": row["student_id"],
                    "name": row["name"],
                    "email": row["email"],
                }
            )

        return students
