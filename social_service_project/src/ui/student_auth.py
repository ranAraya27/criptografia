import customtkinter as ctk
from tkinter import messagebox

from src.backend.auth_service import register_student, login_student
from src.ui.student_dashboard import StudentDashboard


class StudentAuthWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Estudiante - Login / Registro")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(fg_color="#071323")

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Estudiante SISSO",
            font=("Arial", 30, "bold"),
            text_color="white",
        )
        title.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Iniciar sesión o registrarse",
            font=("Arial", 18, "italic"),
            text_color="white",
        )
        subtitle.pack(pady=(0, 25))

        self.tabview = ctk.CTkTabview(
            self,
            width=500,
            height=350,
            fg_color="#1f2937",
            segmented_button_fg_color="#111827",
            segmented_button_selected_color="#b08d18",
            segmented_button_selected_hover_color="#967812",
        )
        self.tabview.pack()

        self.login_tab = self.tabview.add("Login")
        self.signup_tab = self.tabview.add("Sign Up")

        self.create_login_tab()
        self.create_signup_tab()

    def create_login_tab(self):
        self.login_email_entry = ctk.CTkEntry(
            self.login_tab, width=380, height=45, placeholder_text="Correo electrónico"
        )
        self.login_email_entry.pack(pady=(40, 15))

        self.login_password_entry = ctk.CTkEntry(
            self.login_tab,
            width=380,
            height=45,
            placeholder_text="Contraseña",
            show="•",
        )
        self.login_password_entry.pack(pady=15)

        login_button = ctk.CTkButton(
            self.login_tab,
            text="Iniciar sesión",
            width=380,
            height=45,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 16, "bold"),
            command=self.handle_login,
        )
        login_button.pack(pady=20)

    def create_signup_tab(self):
        self.signup_name_entry = ctk.CTkEntry(
            self.signup_tab, width=380, height=45, placeholder_text="Nombre completo"
        )
        self.signup_name_entry.pack(pady=(25, 10))

        self.signup_email_entry = ctk.CTkEntry(
            self.signup_tab, width=380, height=45, placeholder_text="Correo electrónico"
        )
        self.signup_email_entry.pack(pady=10)

        self.signup_password_entry = ctk.CTkEntry(
            self.signup_tab,
            width=380,
            height=45,
            placeholder_text="Contraseña",
            show="•",
        )
        self.signup_password_entry.pack(pady=10)

        signup_button = ctk.CTkButton(
            self.signup_tab,
            text="Registrarse",
            width=380,
            height=45,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 16, "bold"),
            command=self.handle_signup,
        )
        signup_button.pack(pady=15)

    def handle_login(self):
        email = self.login_email_entry.get().strip()
        password = self.login_password_entry.get().strip()

        if not email or not password:
            messagebox.showwarning(
                "Campos incompletos", "Debe ingresar correo y contraseña."
            )
            return

        student = login_student(email, password)

        if student:
            messagebox.showinfo("Login exitoso", f"Bienvenido/a, {student['name']}")
            StudentDashboard(self.master, student)
            self.destroy()
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")

    def handle_signup(self):
        name = self.signup_name_entry.get().strip()
        email = self.signup_email_entry.get().strip()
        password = self.signup_password_entry.get().strip()

        if not name or not email or not password:
            messagebox.showwarning(
                "Campos incompletos", "Debe llenar todos los campos."
            )
            return

        if len(password) < 6:
            messagebox.showwarning(
                "Contraseña débil", "La contraseña debe tener al menos 6 caracteres."
            )
            return

        success = register_student(name, email, password)

        if success:
            messagebox.showinfo(
                "Registro exitoso", "Estudiante registrado correctamente."
            )
            self.tabview.set("Login")
        else:
            messagebox.showerror("Error", "Ese correo ya está registrado.")
