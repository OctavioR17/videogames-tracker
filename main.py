import json

# Cargar juegos desde games.json
try:
	with open("games.json", "r") as file:
		games = json.load(file)
except:
	games = []

while True:
	print("\n=== VIDEOGAMES TRACKER ===")
	print("1. Agregar juego")
	print("2. Ver juegos")
	print("3. Salir")

	option = input("Selecciona una opción: ")

	if option == "1":
		#Pedir datos
		name = input("Nombre del juego: ")
		plataforma = input("Plataforma del juego: ")
		estado = input("Estado del juego: ")

        # Crear diccionario
		game = {
			"nombre": name,
			"plataforma": plataforma,
			"estado": estado
		}

		#Agregar a la lista
		games.append(game)

		#Guardar en el json
		with open("games.json", "w") as file:
			json.dump(games, file, indent=4)

		print("juego agregado")

	elif option == "2":
		print("\nTus juegos:")
		for game in games:
			print(f"""
		 Nombre: {game["nombre"]}
		 Plataforma: {game["plataforma"]}
		 Estado: {game["estado"]}
			""")

	elif option == "3":
		print("Hasta luego")
		break

	else:
		print("Opción no válida")
