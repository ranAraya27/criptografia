import csv
import os
import uuid

PROJECTS_FILE = "data/projects.csv"
HEADERS = ["project_id", "name", "capacity", "available_slots"]


def initialize_projects_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(PROJECTS_FILE) or os.path.getsize(PROJECTS_FILE) == 0:
        with open(PROJECTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        return

    with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
        first_line = file.readline().strip()

    if first_line != ",".join(HEADERS):
        with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
            old_content = file.read()

        with open(PROJECTS_FILE, "w", newline="", encoding="utf-8") as file:
            file.write(",".join(HEADERS) + "\n")
            file.write(old_content)


def create_project(name: str, capacity: int) -> bool:
    initialize_projects_file()

    project_id = str(uuid.uuid4())

    with open(PROJECTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([project_id, name, capacity, capacity])

    return True


def get_all_projects():
    initialize_projects_file()

    with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
