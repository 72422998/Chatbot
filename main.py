from usuarios import acciones


print("""
Acciones disponibles:
      - registro
      - login
""")
hasEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hasEl.registro()
    


elif accion == "login":
    hasEl.login()