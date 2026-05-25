import customtkinter as ctk
from tkinter import messagebox

from src.ui.manager_dashboard import ManagerDashboard


class ManagerLoginWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Gestor - Login")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(fg_color="#071323")

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self, text="Gestor SISSO", font=("Arial", 32, "bold"), text_color="white"
        )
        title.pack(pady=(40, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Iniciar Sesión",
            font=("Arial", 20, "italic"),
            text_color="white",
        )
        subtitle.pack(pady=(0, 30))

        form_frame = ctk.CTkFrame(
            self, width=500, height=300, corner_radius=15, fg_color="#1f2937"
        )
        form_frame.pack()
        form_frame.pack_propagate(False)

        user_label = ctk.CTkLabel(
            form_frame,
            text="Usuario:",
            font=("Arial", 18, "bold"),
            text_color="white",
            anchor="w",
        )
        user_label.pack(pady=(25, 5), padx=35, anchor="w")

        self.username_entry = ctk.CTkEntry(
            form_frame, width=430, height=45, placeholder_text="Ingrese el usuario"
        )
        self.username_entry.pack(pady=(0, 15))

        password_label = ctk.CTkLabel(
            form_frame,
            text="Contraseña:",
            font=("Arial", 18, "bold"),
            text_color="white",
            anchor="w",
        )
        password_label.pack(pady=(0, 5), padx=35, anchor="w")

        self.password_entry = ctk.CTkEntry(
            form_frame,
            width=430,
            height=45,
            placeholder_text="Ingrese la contraseña",
            show="•",
        )
        self.password_entry.pack(pady=(0, 20))

        self.password_entry.bind("<Return>", self.handle_login)
        login_button = ctk.CTkButton(
            form_frame,
            text="Iniciar",
            width=430,
            height=45,
            fg_color="#b08d18",
            hover_color="#967812",
            font=("Arial", 17, "bold"),
            command=self.handle_login,
        )
        login_button.pack()

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
        # back_button.pack(anchor="nw", padx=15, pady=10)
        back_button.place(x=250, y=450)
        
    def handle_login(self,event=None):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login exitoso", "Bienvenido, gestor.")
            ManagerDashboard(self.master)
            self.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def go_back(self):
        if self.master:
            self.master.deiconify()  # Mostrar ventana padre
        self.destroy()
    
    # En MainWindow, override para cerrar todo:
    def close_app(self):
        self.quit()
        self.destroy()