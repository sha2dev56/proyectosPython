def contar_palabras(texto):
    limpio = texto.strip()
    return len(limpio.split())

frase = "Python aplicado a la IA"
cantidad = contar_palabras(frase)
print("El número de palabras en la frase es:", cantidad)
