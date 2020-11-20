from gfxhat import lcd, fonts
from PIL import Image,ImageFont,ImageDraw
from click import getchar

f1 = [ [1,1,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    [0,1,1,1,1,1,1,0], 
    [1,0,1,1,1,1,0,1], 
    [1,0,0,1,1,0,0,1], 
    [1,0,0,1,1,0,0,1], 
    [0,0,0,1,1,0,0,0], 
    [0,0,0,0,0,0,0,0] ]  #elephant
pm = [[0,0,0,1,1,1,1,1,0,0,0], 
    [0,0,1,1,1,1,1,1,1,0,0], 
    [0,1,1,1,1,1,1,1,1,1,0], 
    [1,1,1,1,1,1,1,1,0,0,0], 
    [1,1,1,1,1,1,1,0,0,0,0], 
    [1,1,1,1,1,1,0,0,0,0,0], 
    [1,1,1,1,1,1,0,0,0,0,0], 
    [1,1,1,1,1,1,1,0,0,0,0], 
    [1,1,1,1,1,1,1,1,0,0,0], 
    [0,1,1,1,1,1,1,1,1,1,0], 
    [0,0,1,1,1,1,1,1,1,0,0], 
    [0,0,0,1,1,1,1,1,0,0,0] ] # half circle



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

displayObject(pm,10,15)
