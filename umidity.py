import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

try:
    f = open('/home/pi/umidade.csv', 'a+')
    if os.stat('/home/pi/umidade.csv').st_size == 0:
            f.write('Data,Hora,Temperatura,Umidadern')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%rn'.format(time.strftime('%m/%d/%y'
), time.strftime('%H:%M'), temperature, humidity))
        print("umidade ",humidity," temp",temperature, time.strftime('%m/%d/%y'), time.strftime('%H:%M'))

    else:
        print("Falha ao receber os dados do sensor de umidade ",temperature, humidity)

    time.sleep(30)


