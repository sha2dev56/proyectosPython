
import json

historial = [
    {"role": "user", "content": "Hola"},
    {"role": "assistant", "content": "Hola, ¿cómo estás?"},
    {"role": "user", "content": "Me llamo Carlos"},
    {"role": "assistant", "content": "Encantado, Carlos"},
    {"role": "user", "content": "¿Qué es Python?"},
    {"role": "assistant", "content": "Python es un lenguaje de programación"},
    {"role": "user", "content": "¿Para qué sirve?"},
    {"role": "assistant", "content": "Sirve para desarrollar programas"},
    {"role": "user", "content": "Gracias"},
    {"role": "assistant", "content": "¡De nada!"}
]

with open("historial.json", "w", encoding="utf-8") as archivo:
    json.dump(historial, archivo, indent=4, ensure_ascii=False)

print("Historial creado correctamente")
