import customtkinter as ctk
from tkinter import messagebox

from src.backend.project_service import create_project, get_all_projects
from src.backend.student_service import get_all_students
from src.backend.enrollment_service import (
    get_enrollments_by_project,
    verify_enrollment_hmac,
    verify_enrollment_signature,
)


class ManagerDashboard(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Panel del Gestor")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(fg_color="#071323")

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Panel del Gestor",
            font=("Arial", 32, "bold"),
            text_color="white",
        )
        title.pack(pady=(25, 15))

        self.tabview = ctk.CTkTabview(
            self,
            width=920,
            height=520,
            fg_color="#1f2937",
            segmented_button_selected_color="#b08d18",
            segmented_button_selected_hover_color="#967812",
        )
        self.tabview.pack()

        self.projects_tab = self.tabview.add("Proyectos")
        self.students_tab = self.tabview.add("Estudiantes")

        self.create_projects_tab()
        self.create_students_tab()

    def create_projects_tab(self):
        form_frame = ctk.CTkFrame(
            self.projects_tab, fg_color="#111827", corner_radius=15
        )
        form_frame.pack(pady=15, padx=20, fill="x")

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
            self.projects_tab,
            width=850,
            height=350,
            fg_color="#111827",
            corner_radius=15,
        )
        self.projects_frame.pack(pady=10)

        self.load_projects()

        back_button = ctk.CTkButton(
            self,
            text="← Atrás",
            width=80,
            height=35,
            fg_color="#666666",
            hover_color="#555555",
            font=("Arial", 12),
            command=self.go_back
        )
        back_button.pack(anchor="nw", padx=15, pady=10)

    def create_students_tab(self):
        self.students_frame = ctk.CTkScrollableFrame(
            self.students_tab,
            width=850,
            height=430,
            fg_color="#111827",
            corner_radius=15,
        )
        self.students_frame.pack(pady=25)

        self.load_students()

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
            label = ctk.CTkLabel(
                self.projects_frame,
                text="No hay proyectos registrados.",
                font=("Arial", 16),
                text_color="white",
            )
            label.pack(pady=20)
            return

        for project in projects:
            card = ctk.CTkFrame(
                self.projects_frame, fg_color="#1f2937", corner_radius=12
            )
            card.pack(fill="x", padx=15, pady=10)

            project_title = ctk.CTkLabel(
                card,
                text=project["name"],
                font=("Arial", 20, "bold"),
                text_color="white",
                anchor="w",
            )
            project_title.pack(padx=20, pady=(12, 3), anchor="w")

            info = ctk.CTkLabel(
                card,
                text=f"Cupo total: {project['capacity']} | Cupos disponibles: {project['available_slots']}",
                font=("Arial", 15),
                text_color="white",
            )
            info.pack(padx=20, pady=(0, 8), anchor="w")

            enrolled_students = get_enrollments_by_project(project["project_id"])

            if not enrolled_students:
                enrolled_label = ctk.CTkLabel(
                    card,
                    text="Estudiantes inscritos: ninguno",
                    font=("Arial", 14),
                    text_color="#d1d5db",
                )
                enrolled_label.pack(padx=20, pady=(0, 12), anchor="w")
            else:
                title = ctk.CTkLabel(
                    card,
                    text="Estudiantes inscritos:",
                    font=("Arial", 14, "bold"),
                    text_color="#d1d5db",
                )
                title.pack(padx=20, pady=(0, 5), anchor="w")

                for enrollment in enrolled_students:
                    hmac_valid = verify_enrollment_hmac(enrollment)
                    signature_valid = verify_enrollment_signature(enrollment)

                    hmac_text = (
                        "Registro íntegro" if hmac_valid else "Registro alterado"
                    )
                    signature_text = (
                        "Firma válida" if signature_valid else "Firma inválida"
                    )

                    student_label = ctk.CTkLabel(
                        card,
                        text=f"- {enrollment['student_name']} | {enrollment['student_email']} | {signature_text} | {hmac_text}",
                        font=("Arial", 14),
                        text_color="#d1d5db",
                    )
                    student_label.pack(padx=35, pady=(0, 4), anchor="w")

    def load_students(self):
        for widget in self.students_frame.winfo_children():
            widget.destroy()

        students = get_all_students()

        if not students:
            label = ctk.CTkLabel(
                self.students_frame,
                text="No hay estudiantes registrados.",
                font=("Arial", 16),
                text_color="white",
            )
            label.pack(pady=20)
            return

        for student in students:
            card = ctk.CTkFrame(
                self.students_frame, fg_color="#1f2937", corner_radius=12
            )
            card.pack(fill="x", padx=15, pady=10)

            name_label = ctk.CTkLabel(
                card,
                text=student["name"],
                font=("Arial", 18, "bold"),
                text_color="white",
            )
            name_label.pack(padx=20, pady=(12, 3), anchor="w")

            email_label = ctk.CTkLabel(
                card, text=student["email"], font=("Arial", 14), text_color="#d1d5db"
            )
            email_label.pack(padx=20, pady=(0, 12), anchor="w")

    def go_back(self):
        if self.master:
            self.master.deiconify()  # Mostrar ventana padre
        self.destroy()
    
    # En MainWindow, override para cerrar todo:
    def close_app(self):
        self.quit()
        self.destroy()