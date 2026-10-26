Parcial1 = float(input("Nota de la primera parcial"))
Parcial2 = float(input("Nota de la segunda parcial"))
Parcial3 = float(input("Nota de la tercera parcial"))
Examen = float(input("Nota del examen final"))
Trabajo = float(input("Nota del tabajo final"))
Parcial_total = Parcial1 + Parcial2 + Parcial3
Parcial_porcentaje = Parcial_total * 0.55
Parcial_porcentaje_final = Parcial_total - Parcial_porcentaje 
Examen_porcentaje = Examen * 0.30
Examen_porcentaje_final = Examen - Examen_porcentaje
Trabajo_porcentaje = Trabajo * 0.15
Trabajo_porcentaje_final = Trabajo - Trabajo_porcentaje
Nota_final = (Parcial_porcentaje_final + Examen_porcentaje_final + Trabajo_porcentaje_final) / 3
print ("La nota final es", Nota_final)