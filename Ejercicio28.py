inferior = int(input("Introduce el limite inferior: "))
superior = int(input("Introduce el limite superior: "))

while inferior >= superior:
    print("Error: el inferior debe ser menor que el superior")
    inferior = int(input("Introduce el limite inferior: "))
    superior = int(input("Introduce el limite superior: "))

suma_dentro = 0
fuera = 0
iguales_limite = 0

numero = int(input("Introduce un numero (0 para terminar): "))

while numero != 0:
    if numero > inferior and numero < superior:
        suma_dentro = suma_dentro + numero
    elif numero == inferior or numero == superior:
        iguales_limite = iguales_limite + 1
    else:
        fuera = fuera + 1

    numero = int(input("Introduce un numero (0 para terminar): "))

print("Suma de los numeros dentro del intervalo:", suma_dentro)
print("Numeros fuera del intervalo:", fuera)
print("Numeros iguales a los limites:", iguales_limite)