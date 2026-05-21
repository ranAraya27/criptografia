import customtkinter as ctk
from tkinter import messagebox

from src.backend.project_service import get_all_projects
from src.backend.enrollment_service import enroll_student, student_is_enrolled


class StudentDashboard(ctk.CTkToplevel):
    def __init__(self, master=None, student=None):
        super().__init__(master)

        self.student = student

        self.title("Panel del Participante")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color="#071323")

        self.create_widgets()
        self.load_projects()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text=f"Bienvenido/a, {self.student['name']}",
            font=("Arial", 30, "bold"),
            text_color="white",
        )
        title.pack(pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self, text="Proyectos disponibles", font=("Arial", 20), text_color="white"
        )
        subtitle.pack(pady=(0, 20))

        self.projects_frame = ctk.CTkScrollableFrame(
            self, width=820, height=430, fg_color="#1f2937", corner_radius=15
        )
        self.projects_frame.pack(pady=10)

    def load_projects(self):
        for widget in self.projects_frame.winfo_children():
            widget.destroy()

        projects = get_all_projects()

        if not projects:
            empty_label = ctk.CTkLabel(
                self.projects_frame,
                text="No hay proyectos disponibles.",
                font=("Arial", 16),
                text_color="white",
            )
            empty_label.pack(pady=20)
            return

        already_enrolled = student_is_enrolled(self.student["student_id"])

        for project in projects:
            card = ctk.CTkFrame(
                self.projects_frame, fg_color="#111827", corner_radius=12
            )
            card.pack(fill="x", padx=15, pady=10)

            name_label = ctk.CTkLabel(
                card,
                text=project["name"],
                font=("Arial", 20, "bold"),
                text_color="white",
                anchor="w",
            )
            name_label.pack(padx=20, pady=(12, 3), anchor="w")

            slots_label = ctk.CTkLabel(
                card,
                text=f"Cupos disponibles: {project['available_slots']} de {project['capacity']}",
                font=("Arial", 15),
                text_color="white",
                anchor="w",
            )
            slots_label.pack(padx=20, pady=(0, 8), anchor="w")

            button = ctk.CTkButton(
                card,
                text="Inscribirse",
                width=180,
                height=38,
                fg_color="#b08d18",
                hover_color="#967812",
                font=("Arial", 15, "bold"),
                command=lambda p_id=project["project_id"]: self.handle_enrollment(p_id),
            )
            button.pack(padx=20, pady=(0, 15), anchor="e")

            if already_enrolled or int(project["available_slots"]) <= 0:
                button.configure(state="disabled")

    def handle_enrollment(self, project_id):
        success, message = enroll_student(self.student, project_id)

        if success:
            messagebox.showinfo("Inscripción exitosa", message)
        else:
            messagebox.showwarning("No se pudo inscribir", message)

        self.load_projects()
