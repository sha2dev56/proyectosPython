
import json

with open("historial.json", "r", encoding="utf-8") as archivo:
    historial = json.load(archivo)

role_buscado = input("Introduce el role (user/assistant): ")
print("\nMensajes encontrados:")

for mensaje in historial:
    if mensaje["role"] == role_buscado:
        print(mensaje["content"])
