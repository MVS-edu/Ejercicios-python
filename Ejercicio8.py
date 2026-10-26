sueldo_base = float(input("Introduce tu sueldo base: "))
venta1 = float(input("Introduce la cantidad de tu primera venta: "))
venta2 = float(input("Introduce la cantidad de tu segunda venta: "))
venta3 = float(input("Introduce la cantidad de tu tercera venta: "))
total_ventas = venta1 + venta2 + venta3
comisiones = total_ventas * 0.10
total_mes = sueldo_base + comisiones
print("El total de tus ventas es:", total_ventas)
print("Lo que ganaras por comisiones (10%) es:", comisiones)
print("El total que recibiras este mes es:", total_mes)