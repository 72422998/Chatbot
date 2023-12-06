from datetime import datetime
import re
import random
import tkinter as tk
import mysql.connector
from usuarios.acciones import Acciones
from interfaz import InterfazPrincipal

class BotWindow:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Bartolito")
        self.root.geometry("850x470")

        self.chat_display = tk.Text(self.root, wrap=tk.WORD, bg="#e9ebee", padx=10, pady=10)
        self.chat_display.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_display.yview)

        self.user_input = tk.Entry(self.root, width=74, bd=2, relief=tk.FLAT, font=('Arial', 12), insertbackground="black")
        self.user_input.pack(pady=10, padx=10, side=tk.LEFT)

        self.send_button = tk.Button(self.root, text="Enviar", command=self.send_message, bg="#0084ff", fg="white",padx=5, pady=5, relief=tk.FLAT)
        self.send_button.pack(pady=10, padx=10, side=tk.RIGHT)

        self.volver_button = tk.Button(self.root, text="Volver", command=self.volver, bg="#008374", fg="white", padx=5, pady=5, relief=tk.FLAT)
        self.volver_button.pack(pady=10, padx=10, side=tk.LEFT)

        self.messages = []
        self.user_id = user_id
        self.connection = self.conectar()

    def conectar(self):
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="chat_bot",
            port=3306
        )

        cursor = database.cursor(buffered=True)

        return [database, cursor]

    def get_response(self, user_input):
        split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        return response

    def message_probability(self, user_message, recognized_words, single_response=False, required_word=[]):
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognized_words:
                message_certainty += 1

        percentage = float(message_certainty) / float(len(recognized_words))

        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob
            prob = self.message_probability(message, list_of_words, single_response, required_words)
            if prob > highest_prob.get(bot_response, 0):
                highest_prob[bot_response] = prob

        cursor = self.connection[1]
        cursor.execute("SELECT keywords, response FROM bot_responses")
        responses = cursor.fetchall()

        for keywords, response_text in responses:
            keywords_list = [kw.strip() for kw in keywords.split(',')]
            response(response_text, keywords_list)

        return self.unknown() if not highest_prob or max(highest_prob.values()) < 1 else max(highest_prob, key=highest_prob.get)

    def unknown(self):
        response = ['no entendi tu consulta', 'No estoy seguro de lo quieres', 'Disculpa, puedes intentarlo de nuevo?'][random.randrange(3)]
        return response

    def send_message(self):
        user_input = self.user_input.get()

        self.messages.append(f"Tu: {user_input}")
        bot_response = self.get_response(user_input)
        self.messages.append(f"Bot: {bot_response}")

        self.chat_display.config(state=tk.NORMAL)
        for message in self.messages:
            self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state=tk.DISABLED)

        user_id = self.user_id
        self.store_conversation(user_id, user_input, bot_response)

        self.user_input.delete(0, tk.END)

    def store_conversation(self, user_id, user_message, bot_response):
        cursor = self.connection[1]
        sql = "INSERT INTO historial (usuario_id, mensaje_usuario, mensaje_bot, fecha) VALUES (%s, %s, %s, %s)"

        current_datetime = datetime.now()
        current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        values = (user_id[0], user_message, bot_response, current_datetime_str)

        cursor.execute(sql, values)
        self.connection[0].commit()

    def cargar(self):
        ruta_icono = "./imagenes/icono3.ico"
        self.root.iconbitmap(ruta_icono)

    def volver(self):
        self.root.destroy()
        root_interfaz = tk.Tk()
        app_interfaz = InterfazPrincipal(root_interfaz)
        root_interfaz.mainloop()

    def __del__(self):
        if self.connection[0]:
            self.connection[0].close()

def main():
    acciones = Acciones()
    user_id = acciones.login()[0]
    if user_id:
        root = tk.Tk()
        app = BotWindow(root, user_id)
        app.cargar()
        root.mainloop()
    else:
        print("Error en el inicio de sesión.")

if __name__ == "__main__":
    main()
