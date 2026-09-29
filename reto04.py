##if elif else
prioridad = int(input("Prioridad 1-5): "))
if prioridad >= 4:
    print("Atencion inmediata")
elif prioridad == 3:
    print("Atención normal")    
else:
    print("Baja prioridad")

##practica 1

temperatura= float(input("Indique la temperatura: "))

if temperatura <15:
    print("Temperatura baja")
elif temperatura <=25:
     print("Temperatura normal")
else:
    print("Temperatura alta")

## operadores logicos
score= 0.86
contiene_datos = True
fuente_conocida = True

es_confiable = score and fuente_conocida
requiere_revision = not es_confiable or contiene_datos
print(es_confiable)
print(requiere_revision)
