import tkinter as tk
from tkinter import messagebox
from usuarios.usuario import Usuario
from bot import BotWindow
from interfaz import InterfazPrincipal

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Bartolito")

        # Obtener la resolución de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana
        x = (screen_width - 770) // 2
        y = (screen_height - 470) // 2 + 50  # Mueve el formulario hacia abajo

        # Define la geometría de la ventana
        self.root.geometry(f"770x470+{x}+{y}")

        # Cambia el icono de la ventana
        ruta_icono = "./imagenes/icono3.ico"  # Reemplaza con la ruta de tu nuevo icono
        self.root.iconbitmap(ruta_icono)

        # Crea un lienzo (Canvas) para la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=770, height=470)
        self.canvas.pack()

        # Carga la imagen de fondo
        ruta_imagen_fondo = "./imagenes/fondo2.ppm"  # Reemplaza con la ruta de tu imagen
        self.imagen_fondo = tk.PhotoImage(file=ruta_imagen_fondo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_fondo)

        # Etiqueta principal sin fondo
        self.canvas.create_text(385, 50, text="Formulario de Inicio de Sesión", font=("Helvetica", 20, "bold"), fill="black", anchor=tk.CENTER)

        # Cuadro de Email
        self.email_label = self.canvas.create_text(270, 140, text="Email:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.email_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.email_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Cuadro de Contraseña
        self.password_label = self.canvas.create_text(260, 188, text="Contraseña:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.password_entry = tk.Entry(self.root, show="*", font=("Helvetica", 10))
        self.password_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Button login
        self.login_button = tk.Button(self.root, text="Iniciar Sesión", bg="#008374", fg="white", padx=5, pady=5, command=self.login)
        self.login_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Botón Volver
        self.volver_button = tk.Button(self.root, text="Volver", bg="#008374", fg="white", padx=5, pady=5, command=self.volver)
        self.volver_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Por favor, ingresa tu email y contraseña.")
            return

        user = Usuario('', '', email, password)
        user_id = user.indentificar()

        if user_id:
            # Si el inicio de sesión fue exitoso, cierra la ventana de inicio de sesión
            self.root.destroy()
            # Luego, abre la ventana de Bot y pasa la ID del usuario
            bot_root = tk.Tk()
            bot_app = BotWindow(bot_root, user_id)
            bot_root.mainloop()
        else:
            messagebox.showerror("Error", "Login incorrecto. Por favor, inténtalo de nuevo.")
            
    def volver(self):
        # Cierra la ventana actual
        self.root.destroy()

        # Abre la ventana de InterfazPrincipal
        interfaz_root = tk.Tk()
        interfaz_app = InterfazPrincipal(interfaz_root)
        interfaz_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
