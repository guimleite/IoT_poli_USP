# Programa : Sensor de temperatura DHT11 com Raspberry Pi
# Autor : FILIPEFLOP
 
# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
 
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25
 
# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade");
 
while(1):
   # Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print(temp, umid)
     print(type(temp), type(umid))
     print (f"Temperatura = {temp}  Umidade = {umid}")
     #print ("Temperatura =", temp,  "Umidade =", umid)
     print ("Aguarda 5 segundos para efetuar nova leitura...")
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")