## práctica 1
## print("Python se utiliza para:")
## print("machine learning")
## print("deep learning")
## print("creación de chatbots, generacion de textos...")  

##practica 2

uso1 = "machine learning"
uso2 = "deep learning"
uso3 = "creación de chatbots, generacion de textos..."

print(f"Python se utiliza para: {uso1}, {uso2}, {uso3}.")
##pratica 1
nIncidencias: int
tiempoMedio: float
categoria: str
estadoCerrado: bool
nIncidencias = 5
tiempoMedio = 2.5
categoria = "Software"
estadoCerrado = True

for valor in [nIncidencias, tiempoMedio, categoria, estadoCerrado]:
    print(f"El valor es: {valor} y su tipo es: {type(valor)}")

## practica 2

total: float
precio: float = 19.95
unidades: int = 3
total = precio * unidades
print(f"El total es: {total}€")

##practica 3

nombre = input("Nombre: ")
horas = float(input("Horas de estudio: "))
dias= int(input("Número de días: "))

media = horas /dias
print(f"Hola {nombre}, has estudiado una media de {media} horas por día.")

##practica 4

minutos = int (input ("Introduce el número de minutos para realizar una tarea: "))
horas = minutos // 60
print(f"El número de horas es: {horas} horas")

##practica 5

nombre = input("Como te llamas?")
modulo = input ("Qué módulo estás cursando?")
nota = float(input("Qué nota has sacado?"))
print(f"{nombre}, en el módulo {modulo} has sacado una nota de {nota}.")

##practica 6
total = 0
for i in range (1,11):
    print(f"El múltiplo de 9 es: {i*9}")
    total += i*9
