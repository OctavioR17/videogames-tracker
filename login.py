user = input("Ingresa tu usuario: ")
userpass = input("Ingresa tu contraseña: ")

if((user == "Octavio") and (userpass == "hola")):
    try:
        archivo = open("Tus_juegos.txt", "r")
        print(archivo.read())
        archivo.close()
    except(FileNotFoundError):
        print("Sin registro")

elif user != 'Octavio' or userpass != 'hola':
    print("Usuario no registrado")