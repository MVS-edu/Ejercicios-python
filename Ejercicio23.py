suma = 0
contador = 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1
if contador > 0:
    media = suma / contador
    print(f"La suma es {suma} y la media es {media}")
else:
    print("No se introdujeron números.")