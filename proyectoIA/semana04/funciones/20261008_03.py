#def normaliza_nombre(nombre):
#     limpio = nombre.strip().capitalize()
#     return limpio

# resultado = normaliza_nombre(input("Ingrese su nombre: "))
# print(resultado)

# def mayuscula(nombre):
#     return nombre.strip().upper()

def saludar(nombre):
    mensaje = "Hola, " + nombre + ". Bienvenida al proyecto de IA."
    return mensaje

def primera_letra_mayuscula(nombre):
    nombre = nombre.strip()
    nombre = nombre[0].upper() + nombre[1:]
    return nombre

resultado = input("Ingrese su nombre: ")
texto = saludar(primera_letra_mayuscula(resultado))
print(texto)

# def prueba(nombre):
#     nombre_mayuscula = mayuscula(nombre)
#     print(f"Nombre en mayúsculas: {nombre_mayuscula}")