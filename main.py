games = []

while True:
	print("\n=== VIDEOGAMES TRACKER ===")
	print("1. Agregar juego")
	print("2. Ver juegos")
	print("3. Salir")

	option = input("Selecciona una opción: ")

	if option == "1":
		game = input("Nombre del juego: ")
		games.append(game)
		print("Juego agregado")
	
	elif option == "2":
		print("\nTus juegos:")
		for game in games:
			print("-", game)

	elif option == "3":
		print("Hasta luego")
		break

	else:
		print("Opción no válida")
