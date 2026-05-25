# Social Service Project - SISSO

Student Mobility Management System (SISSO) developed in Python using `CustomTkinter`.

This project simulates a social service fair where students can register, log in, and enroll in social service projects, while an administrative manager can create projects and monitor student enrollments.

Additionally, the system incorporates several cryptographic mechanisms to improve security, including:

- Secure password hashing using `bcrypt`
- Digital signatures using `Ed25519`
- Integrity validation using `HMAC-SHA256`

---

# Main Features

## Student

- User registration
- Login system
- View available projects
- Project enrollment
- Restriction to a single enrollment per student
- Automatic slot validation

## Manager

- Administrative login
- Project creation
- View registered students
- View enrolled students by project
- Digital signature verification
- Record integrity verification

---

# Technologies Used

- Python 3.11
- CustomTkinter
- CSV-based persistent storage
- bcrypt
- cryptography
- HMAC-SHA256
- Ed25519 Digital Signatures

---

# Project Structure

```txt
SOCIAL_SERVICE_PROJECT/
│
├── data/
│   ├── keys/
│   │   └── Cryptographic key files
│   │
│   ├── enrollments.csv
│   ├── projects.csv
│   └── students.csv
│
├── src/
│   │
│   ├── backend/
│   │   ├── auth_service.py
│   │   ├── enrollment_service.py
│   │   ├── project_service.py
│   │   └── student_service.py
│   │
│   ├── crypto/
│   │   ├── hmac_utils.py
│   │   ├── password_utils.py
│   │   └── signature_utils.py
│   │
│   ├── report/
│   │   └── project_report.md
│   │
│   └── ui/
│       ├── main_window.py
│       ├── manager_dashboard.py
│       ├── manager_login.py
│       ├── student_auth.py
│       └── student_dashboard.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

# Folder Explanation

## `/data`

Contains all persistent system files.

### `students.csv`

Stores registered student information.

### `projects.csv`

Stores social service projects.

### `enrollments.csv`

Stores project enrollment records.

### `/keys`

Contains cryptographic keys used by the system.

---

## `/src/backend`

Contains the main business logic of the system.

### `auth_service.py`

Handles student authentication and registration.

### `project_service.py`

Handles project creation and retrieval.

### `enrollment_service.py`

Handles student enrollments.

### `student_service.py`

Handles student information management.

---

## `/src/crypto`

Contains all cryptographic utilities.

### `password_utils.py`

Handles password hashing and verification using `bcrypt`.

### `signature_utils.py`

Handles digital signature generation and verification using `Ed25519`.

### `hmac_utils.py`

Handles HMAC generation and validation using `SHA-256`.

---

## `/src/ui`

Contains all graphical user interfaces.

### `main_window.py`

Main system window.

### `manager_login.py`

Manager login window.

### `manager_dashboard.py`

Administrative dashboard.

### `student_auth.py`

Student login and registration window.

### `student_dashboard.py`

Student dashboard.

---

# Project Dependencies

The project uses the following libraries:

```txt
customtkinter
bcrypt
cryptography
```

---

# Installation

## 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
```

---

## 2. Enter the project folder

```bash
cd social_service_project
```

---

## 3. Create a virtual environment (optional but recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Program

Run the following command:

```bash
python main.py
```

---

# General System Usage

## Main Access Window

When the system starts, the user can choose between:

- Manager
- Student

---

## Manager

Default credentials:

```txt
Username: admin
Password: admin
```

The manager can:

- Create projects
- View registered students
- View enrolled students by project
- Verify enrollment integrity and authenticity

---

## Student

Students can:

- Register
- Log in
- View available projects
- Enroll in a project

Restrictions:

- A student can only enroll in one project
- Project capacity cannot be exceeded

---

# Implemented Security Features

## Password Hashing

Passwords are never stored in plain text.

The system uses `bcrypt` for secure password hashing.

---

## Digital Signatures

Each student has a cryptographic key pair:

- Private key
- Public key

Enrollment records are digitally signed using `Ed25519`.

This allows verification of:

- Authenticity
- Integrity of enrollment records

---

## HMAC

Each enrollment record generates an `HMAC-SHA256`.

This mechanism allows detection of unauthorized modifications to stored records.

---

♡ ***Project developed with love for the Cryptography course*** ♡
