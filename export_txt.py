import json

try:

    #Abrimos JSON
    with open("games.json", "r") as file:
        games = json.load(file)

    #Creamos TXT
    with open("Tus_juegos.txt", "w") as txt:
        txt.write("Tu listado\n")

        for game in games:
            txt.write(f"""
                      Nombre: {game["nombre"]}
                      Plataforma: {game["plataforma"]}
                      Estado: {game["estado"]}
                      """)
            
            print("Archivo TXT generado con exito")

except FileNotFoundError:
    print("No existe games.json")