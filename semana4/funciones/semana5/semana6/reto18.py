import json

historial = [
    {
        "role": "user",
        "content": "Hola, ¿qué tal?"
    },
    {
        "role": "assistant",
        "content": "¡Hola! Estoy muy bien."
    }
]

with open("historial.json", "w", encoding="utf-8") as archivo:
    json.dump(historial, archivo, indent=4, ensure_ascii=False)

with open("historial.json", "r", encoding="utf-8") as archivo:
    historial_cargado = json.load(archivo)

print(historial_cargado[-1]["content"])

