def limpiar(texto):
    return texto.replace("\n", " ")  
def esta_vacio(texto):
    return limpiar(texto) == "hola mundo"
entrada = "hola\nmundo"
print(esta_vacio(entrada))