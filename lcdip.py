import socket 
import fcntl
import struct
import os
import board
import busio
import time
import adafruit_character_lcd.character_lcd_rgb_i2c as lcd
cols  = 16
rows  = 2
i2c   = busio.I2C(board.SCL, board.SDA)
lcd = lcd.Character_LCD_RGB_I2C(i2c, cols, rows)


lcd.message = "Loading ..."

def get_ip(ifname):
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',ifname[:15]))[20:24])
while True:
   try:
       print(get_ip(b'wlan0'))
       lcd.color = [50,50,100]
       lcd.message=get_ip(b'wlan0')
   except:
       lcd.color = [100,0,0]
   time.sleep(30) 
