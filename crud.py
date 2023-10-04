import mysql.connector
import os

os.system('cls')

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='chat_bot',
        user='root',
        password='',
        port=3306
    )
    print("Conexión exitosa!")

except mysql.connector.Error as e:
    print("Error en la consulta", e)

def insert_into(_connection, _nombre, _apellidos, _email, _password):
    sql_insert_Query = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, NOW())"
    cursor = _connection.cursor()
    cursor.execute(sql_insert_Query, (_nombre, _apellidos, _email, _password))
    _connection.commit()
    print("Registro insertado!")

def select(_connection):
    sql_select_Query = "SELECT * FROM usuarios"
    cursor = _connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for row in records:
        print("ID = ", row[0])
        print("Nombre = ", row[1])
        print("Apellidos = ", row[2])
        print("Email = ", row[3])
        print("Contraseña = ", row[4])
        print("Fecha = ", row[5], "\n")

def update(_connection, _email, _new_password):
    sql_update_Query = "UPDATE usuarios SET password = %s WHERE email = %s"
    cursor = _connection.cursor()
    cursor.execute(sql_update_Query, (_new_password, _email))
    _connection.commit()
    print("Registro actualizado!")

def delete(_connection, _email):
    sql_delete_Query = "DELETE FROM usuarios WHERE email = %s"
    cursor = _connection.cursor()
    cursor.execute(sql_delete_Query, (_email,))
    _connection.commit()
    print("Registro eliminado!")

def menu_opciones():
    print("INICIO del CRUD")
    print("=====================")
    print("[1] Insertar")
    print("[2] Seleccionar")
    print("[3] Modificar contraseña")
    print("[4] Eliminar")
    print("[5] Salir del programa")
    print("=====================")

op = 1
while op != 5:
    menu_opciones()
    op = int(input("Ingrese una opción: "))
    print("=====================")

    if op == 1:
        print("Ingrese los datos del usuario")
        _nombre = input("Nombre: ")
        _apellidos = input("Apellidos: ")
        _email = input("Email: ")
        _password = input("Contraseña: ")
        insert_into(connection, _nombre, _apellidos, _email, _password)

    elif op == 2:
        select(connection)

    elif op == 3:
        print("Modificar contraseña de usuario")
        _email = input("Email del usuario: ")
        _new_password = input("Nueva contraseña: ")
        update(connection, _email, _new_password)

    elif op == 4:
        print("Eliminar registro de usuario")
        _email = input("Email del usuario: ")
        delete(connection, _email)

    elif op == 5:
        print("FIN del CRUD")
        break

    print("===================================")
    rpt = input("¿Desea regresar al menú de opciones? s/n: ")

    if rpt == "s":
        os.system('cls')  # Limpiar la consola en Windows
    else:
        exit()

else:
    print("FIN del CRUD")