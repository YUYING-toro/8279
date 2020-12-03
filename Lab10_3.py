from gfxhat import lcd, fonts
from PIL import Image,ImageFont,ImageDraw
from click import getchar
import textwrap
from pprint import pprint


def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            if x2 == 1:
                pixel = 1
            else:
                pixel = 0
            lcd.set_pixel(xp, y, pixel)
            xp += 1
        y += 1
        lcd.set_pixel(xp, y, pixel)
        xp = x
    lcd.show()

f=open('/home/pi/Documents/python/1127_PY_Lab10/font3.txt','r')


bmaps = {}
for line in f:  # open('file')
    hex_val, char = line.strip().split(',', maxsplit=1)
    bits = bin(int(hex_val, 16))[2:].zfill(64)
    m = [list(map(int, line)) for line in textwrap.wrap(bits, 8)]
    bmaps[char] = m


def etchSketch(x,y):
    while True:
        key = getchar()

        # displayObject(toro,x,y)
        
        if key in  bmaps.keys(): #[key1key2....]
            displayObject(bmaps[key],x,y)
            lcd.show()

      
        if key == 'q': #quit or start
            lcd.clear()
            lcd.show()


etchSketch(10,30)


