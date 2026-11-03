base = float(input("Introduce la base (real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

resultado = 1

for i in range(exponente):
    resultado = resultado * base

print(base, "elevado a", exponente, "es", resultado)