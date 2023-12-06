import tkinter as tk

class InterfazPrincipal:
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

        # Etiqueta principal con texto (superpuesta en el Canvas)
        self.canvas.create_text(385, 50, text="¡Bienvenido a Bartolito!", font=("Helvetica", 20, "bold"), fill="black", anchor=tk.CENTER)

        # Botón para abrir la ventana de inicio de sesión
        self.login_button = tk.Button(self.root, text="Iniciar Sesión", bg="#008374", fg="white", padx=5, pady=5, command=self.abrir_ventana_login)
        self.login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Botón para abrir la ventana de registro
        self.register_button = tk.Button(self.root, text="Registrar", bg="#008374", fg="white", padx=5, pady=5, command=self.abrir_ventana_registro)
        self.register_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def abrir_ventana_login(self):
        from login_window import LoginWindow  # Importa aquí para evitar importación circular
        # Cierra la ventana actual
        self.root.destroy()

        # Abre la ventana de inicio de sesión
        login_root = tk.Tk()
        login_app = LoginWindow(login_root)
        login_root.mainloop()

    def abrir_ventana_registro(self):
        from register_window import RegisterWindow  # Importa aquí para evitar importación circular
        # Cierra la ventana actual
        self.root.destroy()

        # Abre la ventana de registro
        register_root = tk.Tk()
        register_app = RegisterWindow(register_root)
        register_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazPrincipal(root)
    root.mainloop()
