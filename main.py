import tkinter as tk
from interfaz import LoginWindow

chat_on = False

def open_chat():
    global chat_on
    chat_on = True
    login_window.root.destroy()

    # Crear la ventana de chat y demás lógica (como se mostró anteriormente)

if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()

    if chat_on:
        open_chat()
    else:
        print("Debes iniciar sesión para usar el chatbot.")