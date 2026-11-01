numero_secreto = random.randint(1, 100)
intentos = 0
acertado = False
while not acertado and intentos < 10:
    intento = int(input(f"Intento {intentos + 1} de 10. Introduce un número: "))
    intentos += 1
 if intento < numero_secreto:
        print("El número secreto es MAYOR.")
    elif intento > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        acertado = True
        print(f"¡Correcto! Has acertado en {intentos} intentos.")
if not acertado:
    print(f"Te has quedado sin intentos. El número era {numero_secreto}.")