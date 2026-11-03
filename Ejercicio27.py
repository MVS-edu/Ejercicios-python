numero = int(input("Introduce un numero: "))

print("Tabla de multiplicar del", numero)

for i in range(0, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)