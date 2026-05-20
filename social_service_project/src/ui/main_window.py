import customtkinter as ctk

from src.ui.manager_login import ManagerLoginWindow
from src.ui.student_auth import StudentAuthWindow


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SISSO - Sistema de Servicio Social")
        self.geometry("800x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#071323")

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Universidad Nacional Autónoma de México\nServicio Social",
            font=("Arial", 28, "bold"),
            text_color="white",
        )
        title.pack(pady=(50, 10))

        subtitle = ctk.CTkLabel(
            self, text="SISSO", font=("Arial", 70, "bold"), text_color="white"
        )
        subtitle.pack(pady=(60, 0))

        description = ctk.CTkLabel(
            self,
            text="Sistema de Gestión de Servicio Social",
            font=("Arial", 18),
            text_color="white",
        )
        description.pack(pady=(0, 35))

        login_frame = ctk.CTkFrame(
            self, width=580, height=140, corner_radius=15, fg_color="#1f2937"
        )
        login_frame.pack(pady=20)
        login_frame.pack_propagate(False)

        login_label = ctk.CTkLabel(
            login_frame, text="Iniciar Sesión", font=("Arial", 26), text_color="white"
        )
        login_label.pack(pady=(15, 10))

        buttons_frame = ctk.CTkFrame(login_frame, fg_color="transparent")
        buttons_frame.pack(pady=5)

        manager_button = ctk.CTkButton(
            buttons_frame,
            text="Soy gestor",
            width=230,
            height=55,
            corner_radius=10,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 18, "bold"),
            command=self.open_manager_login,
        )
        manager_button.grid(row=0, column=0, padx=8)

        student_button = ctk.CTkButton(
            buttons_frame,
            text="Soy participante",
            width=230,
            height=55,
            corner_radius=10,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 18, "bold"),
            command=self.open_student_options,
        )
        student_button.grid(row=0, column=1, padx=8)

    def open_manager_login(self):
        self.withdraw()
        ManagerLoginWindow(self)

    def open_student_options(self):
        self.withdraw()
        StudentAuthWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
