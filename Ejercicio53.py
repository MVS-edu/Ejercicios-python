n1 = float(input("Nota 1 (0-10): "))
n2 = float(input("Nota 2 (0-10): "))
n3 = float(input("Nota 3 (0-10): "))
n4 = float(input("Nota 4 (0-10): "))
n5 = float(input("Nota 5 (0-10): "))

notas = [n1, n2, n3, n4, n5]

print(f"Todas las notas: {notas}")
print(f"Nota media: {sum(notas)/len(notas)}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")