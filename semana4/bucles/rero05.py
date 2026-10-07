for i in range (5):
    print("Repetición", i)

incidencias = ("red", "impresora", "correo")
for numero, incidencia in enumerate(incidencias, start = 1):
    print(numero, incidencia)

lista = [0.42, 0.91,0.77,0.85,0.99]
for numero in lista:
    if numero >= 0.8:
        print(numero)

textos = ["hola mundo", "python para ia", "dam"]
for texto in textos:
    print(len(texto.split()), texto)