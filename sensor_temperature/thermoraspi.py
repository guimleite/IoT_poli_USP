"Thermoraspi Code"
 
"Libary imports"
import Adafruit_DHT as sensor_DHT
import RPi.GPIO as GPIO
import time
 
"Choose a Sensor"
sensor = sensor_DHT.DHT11
#sensor = sensor_DHT.DHT22
 
"Define the GPIO pin to be used as data"
pin_sensor = 24


"Inicial Setup"
GPIO.setmode(GPIO.BOARD)
print ("Thermoraspi on")
print ("Reading Temperature and Humidity sensor...")

while(1):
   "Reading sensor values"
   humid, temp = sensor_DHT.read_retry(sensor, pin_sensor)
   if humid is not None and temp is not None:
     print (f"Temperature = {temp}  Humidity = {humid}")
     
     "Temperature Classification"
     if temp <= 0:
         print("WARNING: Very Cold Environment (Less than 0C)")
     elif temp <= 10:
         print("Stay Alert: Cold Environment (Less than 10C)")
     elif temp >= 50:
         print("EMERGENCY: SOMETHING MIGHT BE ON FIRE!!! (More than 50C)")
     elif temp >= 40:
         print("WARNING: Very Hot Environment (More than 40C)")
     elif temp >= 30:
         print("Stay Alert: Hot Environment (More than 30C)")

         "Humidity Classification"
     if humid <= 12:
         print("EMERGENCY: TOTALLY DRY ENVIRONMENT!!! (Less than 12%)")
     elif humid <= 20:
         print("WARNING: Very Dry Environment (Less than 20%)")
     elif humid <= 30:
         print("Stay Alert: Dry Environment (Less than 30%)")
     elif humid >= 90:
         print("WARNING: Very Humid Environment (More than 90%)")
     elif humid >= 80:
         print("Stay Alert: Humid Environment (More than 80%)")

     print ("Waiting for updates")
     time.sleep(60)
   else:
     "If sensor was not read properly"
     print("Sensor reading failure")