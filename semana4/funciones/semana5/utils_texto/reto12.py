def pedir_texto():
    return input("Introduce una frase: ")

def limpiar_texto(texto):
    return texto.strip().lower()

def mostrar_resultado(texto):
    print(f"Texto limpio: '{texto}'")

frase= pedir_texto()
frase_limpia = limpiar_texto(frase)
mostrar_resultado(frase_limpia)