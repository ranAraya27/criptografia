import customtkinter as ctk
from tkinter import messagebox

from src.backend.project_service import create_project, get_all_projects


class ManagerDashboard(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Panel del Gestor")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(fg_color="#071323")

        self.create_widgets()
        self.load_projects()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Panel del Gestor",
            font=("Arial", 32, "bold"),
            text_color="white",
        )
        title.pack(pady=(25, 15))

        form_frame = ctk.CTkFrame(self, fg_color="#1f2937", corner_radius=15)
        form_frame.pack(pady=10, padx=40, fill="x")

        form_frame.grid_columnconfigure(0, weight=3)
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(2, weight=1)

        self.project_name_entry = ctk.CTkEntry(
            form_frame, height=45, placeholder_text="Nombre del proyecto"
        )
        self.project_name_entry.grid(row=0, column=0, padx=15, pady=20, sticky="ew")

        self.capacity_entry = ctk.CTkEntry(
            form_frame, height=45, placeholder_text="Cupo"
        )
        self.capacity_entry.grid(row=0, column=1, padx=15, pady=20, sticky="ew")

        create_button = ctk.CTkButton(
            form_frame,
            text="Crear proyecto",
            height=45,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 15, "bold"),
            command=self.handle_create_project,
        )
        create_button.grid(row=0, column=2, padx=15, pady=20, sticky="ew")

        self.projects_frame = ctk.CTkScrollableFrame(
            self, width=780, height=400, fg_color="#1f2937", corner_radius=15
        )
        self.projects_frame.pack(pady=20)

    def handle_create_project(self):
        name = self.project_name_entry.get().strip()
        capacity_text = self.capacity_entry.get().strip()

        if not name or not capacity_text:
            messagebox.showwarning("Campos incompletos", "Debe ingresar nombre y cupo.")
            return

        if not capacity_text.isdigit():
            messagebox.showwarning(
                "Cupo inválido", "El cupo debe ser un número entero."
            )
            return

        capacity = int(capacity_text)

        if capacity <= 0:
            messagebox.showwarning("Cupo inválido", "El cupo debe ser mayor que cero.")
            return

        create_project(name, capacity)

        messagebox.showinfo("Proyecto creado", "El proyecto fue creado correctamente.")

        self.project_name_entry.delete(0, "end")
        self.capacity_entry.delete(0, "end")

        self.load_projects()

    def load_projects(self):
        for widget in self.projects_frame.winfo_children():
            widget.destroy()

        projects = get_all_projects()

        if not projects:
            empty_label = ctk.CTkLabel(
                self.projects_frame,
                text="No hay proyectos registrados.",
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

            capacity_label = ctk.CTkLabel(
                card,
                text=f"Cupo total: {project['capacity']} | Cupos disponibles: {project['available_slots']}",
                font=("Arial", 15),
                text_color="white",
                anchor="w",
            )
            capacity_label.pack(padx=20, pady=(0, 12), anchor="w")
