import json

def cargar_configuracion(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        configuracion = json.load(archivo)

    return configuracion

try:
    datos = cargar_configuracion("config.json")
except Exception as e:
    print(type(e).__module__, type(e).__name__ , e)
    print(type(e). __mro__)
