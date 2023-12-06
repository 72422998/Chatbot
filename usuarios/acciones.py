from usuarios.usuario import Usuario  # Asegúrate de importar la clase Usuario

class Acciones:
    def get_user_id(self, email):
        # Obtener el ID del usuario según su correo electrónico desde la base de datos
        user = Usuario('', '', email, '')  # Ajusta según tu implementación de Usuario
        user_data = user.get_user_data_by_email()
        user_id = user_data[0]  # Supongamos que el ID del usuario está en la primera posición
        return user_id