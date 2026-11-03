num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

for numero in range(menor, mayor + 1):
    if numero % 2 == 0:
        print(numero)