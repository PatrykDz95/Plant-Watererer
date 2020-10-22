import picamera
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from gpiozero import DigitalInputDevice
import os
import time
import Adafruit_DHT
import csv



import spidev
import os
import time
 
delay = 0.2
 
spi = spidev.SpiDev()
spi.open(0,0)

init = False

GPIO.setmode(GPIO.BOARD)
#For the pump
def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
#Turn the pump on
def pump_on(pump_pin=7, delay=1):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(5)
    GPIO.output(pump_pin, GPIO.HIGH)

#reading the values with an A/C MCP3008 between 0 an 1023
#The max value for a dry sensor is 895(for me)
# The clsoer to 0 the more wet the soil is
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data
 
#infinite loop to check the soil
while True:
    val = readChannel(0)
#    if (val != 0):
    print(val)
    time.sleep(delay)
    if(val > 564):
        pump_on(7, 1)
        time.sleep(60)







#DHT_SENSOR = Adafruit_DHT.DHT11
#DHT_PIN = 17
#d0_input = DigitalInputDevice(14)


#with open('/media/pi/INTENSO/humidity.csv', 'w') as csvfile:
#    fieldnames = ['Date','Time','Temperature','Humidity','Watering']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writerow(
#        {'Date': 'Date', 'Time': 'Time',
#         'Temperature': 'Temperature', 'Humidity': 'Humidity', 'Watering':'Watering'})
#    
#    while True:
#        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
#
#        if humidity is not None and temperature is not None:
#            if (not d0_input.value):
#                watering = 'NO'
#            else:
#                watering = 'YES'
#            print('humidity:', "{0:0.1f}".format(humidity), 'temperature:', "{0:0.1f}".format(temperature), 'watering:', watering)
#            writer.writerow({'Date':time.strftime('%m/%d/%y'),'Time': time.strftime('%H:%M'),'Temperature': '{0:0.1f}'.format(temperature), 'Humidity':'{0:0.1f}'.format(humidity),'Watering': watering})
#            csvfile.flush()
#        else:
#            print("Failed to retrieve data from humidity sensor")

#        time.sleep(30)