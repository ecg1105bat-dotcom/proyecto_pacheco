import time, random
from app.services.medicion_service import MedicionService

print("Simulado sensores cada 20 segundos...")
while True:

    temp = round(random.uniform(20, 30), 1)
    hum = round(random.uniform(50, 80), 1)
    ph = round(random.uniform(6, 8), 1)

    MedicionService.guardar_lectura(temp, hum, ph)
    print(f"Guardado: {temp}C, {hum}%, pH{ph}")
    time.sleep(20)