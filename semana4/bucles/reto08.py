puntuacion = float(input("Ingrese una puntuacion entre 0 y 1:"))
while puntuacion < 0 or puntuacion > 1:
    print("Puntuacion no valida")
    puntuacion = float(input("Ingrese una puntuacion entre 0 y 1:"))
print("Puntuacion valida:", puntuacion)