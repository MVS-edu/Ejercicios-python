import time
hora = 0
minuto = 0
segundos = 0

segundos_inicio = 0

while True:
    time.sleep(1)
    segundos_inicio += 1
    hora = segundos_inicio // 3600
    minuto = segundos_inicio % 3600 // 60
    segundos = segundos_inicio % 60
    print (f"time: {hora}:{minuto}:{segundos}")

