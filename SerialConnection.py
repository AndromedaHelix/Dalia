from time import time, sleep, asctime, localtime
import serial

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
print('Opening serial port')
ser = serial('/dev/ttyACM0', 9600, timeout=3)
sleep(1)                      
while 1:
    txt = 'It is about ' + asctime(localtime()) + ' now'
    print('Sending  "{}"'.format(txt))
    ser.write(txt)
    s = ser.readline()       
    print('Readback "{}" at {}'.format(s, asctime(localtime())))
    sleep(1)