total = int(input("¿Cuántos números quieres introducir? "))

positivos = 0
negativos = 0
ceros = 0

for i in range(total):
    numero = int(input(f"Introduce el número {i + 1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")   