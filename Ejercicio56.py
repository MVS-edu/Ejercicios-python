meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero = int(input("Dime mes (1-12): "))

if 1 <= numero <= 12:
    print(f"El mes ({numero}) es {meses[numero - 1]} y tiene {dias[numero - 1]} días")
else:
    print("Mes inválido")