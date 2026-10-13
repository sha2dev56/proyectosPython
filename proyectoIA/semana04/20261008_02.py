def saludar(nombre):
    mensaje = (f"Hola, {nombre}. Bienvenida al proyecto de IA.")
    return mensaje

resultado = saludar(input("Ingrese su nombre: "))
print(resultado)