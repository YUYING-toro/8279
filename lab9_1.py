from gfxhat import lcd, fonts
from PIL import Image,ImageFont,ImageDraw
from click import getchar

# have text

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width,height = lcd.dimensions()
    image = Image.new('P',(width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold , 24)
    w , h = font.getsize(text)
    draw.text((x,y), text ,1,font)
    for x1 in range (x,x+w):
        for y1 in range (y , y+h):
            pixel = image.getpixel((x1,y1))
            lcd.set_pixel(x1,y1,pixel)
    lcd.show()

def etchSketch(x,y):
    while True:
        key = getchar()
        lcd.set_pixel(x,y,1)
        lcd.show()
        if key == 's': # start again a new drawing on the hat
            clearScreen(lcd)
        elif key == '\x1b[A': #up
            y = y-1
            if y ==0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[B': #DOWN:
            y = y + 1
            if y ==63:
                y = 0
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[C': #right:
            x = x + 1
            if x == 127:
                x = 0
                ###
            if x >127 :
                x =0
            if x <0 :
                x =127
                ####

            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[D': #left:
            x = x - 1
            if x == 0:
                x = 127
                 ###
            if x >127 :
                x =0
            if x <0 :
                x =127
                ####
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == 'q': #quit
            lcd.clear()
            lcd.show()
            exit()
        else:
            print('done')


clearScreen(lcd)
displayText('Lab 9' ,lcd,20,10) # when "run" pi shows lab9,and click anything in below terminal,"lab9" gone
# c = click.getchar() # has import click
c = getchar()
etchSketch(4,25)


    