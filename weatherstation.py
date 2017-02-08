from sense_hat import SenseHat
from subprocess import *
import time

sense = SenseHat()
measurements = 0
measurementstemp = 0
mintemp = 1000
maxtemp = -1000
minhum = 100
maxhum = 0
measurementshum = 0
minpres = 1100
maxpres = 800
measurementspres = 0

def gettemp():
    global measurements
    global measurementstemp
    measurements += 1
    t = sense.get_temperature()
    tp = sense.get_temperature_from_pressure()
    cputemp = float(run_cmd("/opt/vc/bin/vcgencmd measure_temp| grep -o '[0-9.]*'"))
    temp = (t+tp)/2
    temp = temp - ((cputemp - temp)/1.8)
    setmintemp(temp)
    setmaxtemp(temp)
    measurementstemp += temp
    return round(temp,1)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def getpressure():
    global measurementspres
    pressure = sense.get_pressure()
    measurementspres += pressure
    setminpres(pressure)
    setmaxpres(pressure)
    return round(pressure,1)

def gethumidity():
    global measurementshum
    humidity = sense.get_humidity()*(2.5-0.029*sense.get_temperature())
    measurementshum += humidity
    setminhum(humidity)
    setmaxhum(humidity)
    return round(humidity,1)

def getavgtemp():
    return round(measurementstemp / measurements,1)

def getavgpres():
    return round(measurementspres / measurements, 1)

def getavghum():
    return round(measurementshum / measurements, 1)

def getmintemp():
    return round(mintemp,1)

def getmaxtemp():
    return round(maxtemp,1)

def getminhum():
    return round(minhum,1)

def getmaxhum():
    return round(maxhum,1)

def getminpres():
    return round(minpres,1)

def getmaxpres():
    return round(maxpres,1)

def setmintemp(temp):
    global mintemp
    if(temp < mintemp):
        mintemp = temp

def setmaxtemp(temp):
    global maxtemp
    if(temp > maxtemp):
        maxtemp = temp

def setminhum(hum):
    global minhum
    if(hum < minhum):
        minhum = hum

def setmaxhum(hum):
    global maxhum
    if(hum > maxhum):
        maxhum = hum

def setminpres(pres):
    global minpres
    if(pres < minpres):
        minpres = pres

def setmaxpres(pres):
    global maxpres
    if(pres > maxpres):
        maxpres = pres
