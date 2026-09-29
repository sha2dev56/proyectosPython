## mensaje = "Error de CONEXIÓN"
## limpio = mensaje.strip().lower()
## palabras = limpio.split()
##print(limpio)
##print(palabras)
##print(f"El mensaje contiene {len(palabras)} palabras.") 

##mensaje = str (input("Introduce un mensaje: "))
##frase = mensaje.strip().lower()
##palabras = frase.split()
## print(f"Frase: {frase}, Número de palabras: {len(palabras)}")

etiqueta = "URGENTE RED"
prioridad, categoria = etiqueta.split()
print(prioridad.lower())
print(categoria.lower())
##partes = etiqueta.split("-")
##uno= partes[0]
##dos= partes[1]
##print(uno,dos)
entrada=input("Dime una frase con guiones: ")
partes= entrada.split("-")
palabras=len(partes)
for valor in range(palabras):
    print(partes[valor])















