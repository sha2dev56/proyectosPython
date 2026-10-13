precioBase = float(input("Precio base: "))

usos = int (input("Numero usos: "))

descuento = 10

totalsinDescuento = precioBase* usos

total = totalsinDescuento - ((totalsinDescuento * 10) / 100)

print(f"Precio final: {total: .2f}")

print(" ")

registros = int(input("Registros: "))

lotes = registros // 32

sobras = registros - lotes* 32 # registros % 32

print(f"Hay {lotes} lotes y sobran {sobras} registros")