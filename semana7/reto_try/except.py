import json
try:
    with open("config.json",encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print("El archivo config.json no se encontró.")
except PermissionError:
    print("No tienes permiso para leer el archivo config.json.")
except json.JSONDecodeError as e:
    print(f"config.json no es JSON valido (linea {e.lineno})")
else:
    print("Configuración cargada correctamente.", config)
finally:
    print("Fin de la ejecución del programa.")