# Written by Juan Pablo Gutiérrez

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import main_page

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '' #COMPLETE WITH YOUR WIFI SSID
password = ''#COMPLETE WITH YOUR WIFI PASSWORD

station = network.WLAN(network.STA_IF)
station.active(True)

if station.isconnected() == False:
    station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)

