import customtkinter as ctk

from src.backend.project_service import get_all_projects


class StudentDashboard(ctk.CTkToplevel):
    def __init__(self, master=None, student=None):
        super().__init__(master)

        self.student = student

        self.title("Panel del Estudiante")
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
            slots_label.pack(padx=20, pady=(0, 12), anchor="w")
