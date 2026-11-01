while True:
    caracter = input("Introduce un carácter (espacio para terminar): ")
 if caracter == " ":
        break
 c = caracter[0].lower()
 if c in "aeiou":
 print("VOCAL")
    else:
        print("NO VOCAL")