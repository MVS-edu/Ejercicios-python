texto2 = "Hola" 

texto = ""
while not texto or texto[:len(texto2)] != texto2:
    texto = input(f"El texto tiene que empezar por:'{texto2}': ")

print("Texto válido:", texto)