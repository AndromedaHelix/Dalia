# Written by Juan Pablo Gutiérrez

try:
  import usocket as socket
except:
  import socket

import network
import esp
import gc
from main_page import *
from machine import Pin


esp.osdebug(None)

gc.collect()

ssid = 'GtzGarcia'
password = 'casa2022'

station = network.WLAN(network.STA_IF)
station.active(True)

if station.isconnected() == False:
    station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

runMain()