import usuarios.usuario as modelo
from getpass import getpass
class Acciones:

    def registro(self):
        print("\nOk!, vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nVale!! Identifícate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = getpass("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            result = usuario.indentificar()

            if result:
                print(f"Bienvenido {result[1]}, te has registrado en el sistema el {result[5]}")
            else:
                print("Login incorrecto!! Inténtalo más tarde")
        except Exception as e:
            print(f"Error en la función login: {str(e)}")


