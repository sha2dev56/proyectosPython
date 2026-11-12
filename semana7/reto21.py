def pedir_temperatura(texto):
    """Convierte el texto en un número entre 0 y 2"""
    valor = float(texto)
    if not 0 <= valor <= 2:
        raise ValueError("La temperatura debe estar entre 0 y 2")
    return valor

try:
    t = pedir_temperatura(input("Introduce la temperatura: "))
except ValueError as e:
    print("Dato no válido:", e)