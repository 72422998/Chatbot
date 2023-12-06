import tkinter as tk
from tkinter import messagebox
from usuarios.usuario import Usuario
from interfaz import InterfazPrincipal

class RegisterWindow:
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
        self.canvas.create_text(385, 50, text="Formulario de Registro", font=("Helvetica", 20, "bold"), fill="black", anchor=tk.CENTER)

        # Campos de entrada sin fondo
        self.canvas.create_text(275, 140, text="Nombre:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.nombre_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.nombre_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.canvas.create_text(275, 189, text="Apellidos:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.apellidos_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.apellidos_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.canvas.create_text(286, 235, text="Email:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.email_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.email_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas.create_text(268, 282, text="Contraseña:", font=("Helvetica", 12), fill="black", anchor=tk.CENTER)
        self.password_entry = tk.Entry(self.root, show="*", font=("Helvetica", 10))
        self.password_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Botón registrar
        self.register_button = tk.Button(self.root, text="Registrar", bg="#008374", fg="white", padx=5, pady=5, command=self.register)
        self.register_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Botón Volver
        self.volver_button = tk.Button(self.root, text="Volver", bg="#008374", fg="white", padx=5, pady=5, command=self.volver)
        self.volver_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def register(self):
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not nombre or not apellidos or not email or not password:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        user = Usuario(nombre, apellidos, email, password)
        registro = user.registrar()

        if registro[0] >= 1:
            messagebox.showinfo("Registro exitoso", f"¡Perfecto, {registro[1].nombre}! Te has registrado con el email {registro[1].email}.")
        else:
            messagebox.showerror("Error", "No te has registrado correctamente. Por favor, inténtalo de nuevo.")

    def volver(self):
        # Cierra la ventana actual
        self.root.destroy()

        # Abre la ventana de InterfazPrincipal
        interfaz_root = tk.Tk()
        interfaz_app = InterfazPrincipal(interfaz_root)
        interfaz_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterWindow(root)
    root.mainloop()
