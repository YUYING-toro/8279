from gfxhat import lcd, fonts
from PIL import Image,ImageFont,ImageDraw
from click import getchar
import textwrap
from pprint import pprint


f=open('/home/pi/Documents/python/1127_PY_Lab10/font3.txt','r')


bmaps = {}
for line in f:  # open('file')
    hex_val, char = line.strip().split(',', maxsplit=1)
    bits = bin(int(hex_val, 16))[2:].zfill(64)
    m = [list(map(int, line)) for line in textwrap.wrap(bits, 8)]
    bmaps[char] = m

# pprint(bmaps)




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



def etchSketch(x,y):
    while True:
        key = getchar()
        # displayObject(toro,x,y)
        # if key == bmaps.get(key):
        #     displayObject(bmaps[key],x,y)
        #     lcd.show()
        if key == '!':
            # print(key,'e')
        #     # print(type(key))
            displayObject(bmaps['!'],x,y)
            lcd.show()
        if key == '"':
            displayObject(bmaps['"'],x,y)
            lcd.show()
        if key == '#':
            displayObject(bmaps['#'],x,y)
            lcd.show()
        if key == '$':
            displayObject(bmaps['$'],x,y)
            lcd.show()
        if key == '%':
            displayObject(bmaps['%'],x,y)
            lcd.show()
        if key == '&':
            displayObject(bmaps['&'],x,y)
            lcd.show()
        # if key == ''':
        #     displayObject(bmaps['''],x,y)
            # lcd.show()
        if key == '(':
            displayObject(bmaps['('],x,y)
            lcd.show()
        if key == ')':
            displayObject(bmaps[')'],x,y)
            lcd.show()
        if key == '*':
            displayObject(bmaps['*'],x,y)
            lcd.show()
        if key == '+':
            displayObject(bmaps['+'],x,y)
            lcd.show()
        if key == '-':
            displayObject(bmaps['-'],x,y)
            lcd.show()
        if key == '.':
            displayObject(bmaps['.'],x,y)
            lcd.show()
        if key == '/':
            displayObject(bmaps['/'],x,y)
            lcd.show()
        if key == '0':
            displayObject(bmaps['0'],x,y)
            lcd.show()
        if key == '1':
            displayObject(bmaps['1'],x,y)
            lcd.show()
        if key == '2':
            displayObject(bmaps['2'],x,y)
            lcd.show()
        if key == '3':
            displayObject(bmaps['3'],x,y)
            lcd.show()
        if key == '4':
            displayObject(bmaps['4'],x,y)
            lcd.show()
        if key == '5':
            displayObject(bmaps['5'],x,y)
            lcd.show()
        if key == '6':
            displayObject(bmaps['6'],x,y)
            lcd.show()
        if key == '7':
            displayObject(bmaps['7'],x,y)
            lcd.show()
        if key == '8':
            displayObject(bmaps['8'],x,y)
            lcd.show()
        if key == '9':
            displayObject(bmaps['9'],x,y)
            lcd.show()
        if key == ':':
            displayObject(bmaps[':'],x,y)
            lcd.show()
        if key == ';':
            displayObject(bmaps[';'],x,y)
            lcd.show()
        if key == '<':
            displayObject(bmaps['<'],x,y)
            lcd.show()
        if key == '=':
            displayObject(bmaps['='],x,y)
            lcd.show()
        if key == '>':
            displayObject(bmaps['>'],x,y)
            lcd.show()
        if key == '?':
            displayObject(bmaps['?'],x,y)
            lcd.show()
        if key == '@':
            displayObject(bmaps['@'],x,y)
            lcd.show()
        if key == 'A':
            displayObject(bmaps['A'],x,y)
            lcd.show()
        if key == 'B':
            displayObject(bmaps['B'],x,y)
            lcd.show()
        if key == 'C':
            displayObject(bmaps['C'],x,y)
            lcd.show()
        if key == 'D':
            displayObject(bmaps['D'],x,y)
            lcd.show()
        if key == 'E':
            displayObject(bmaps['E'],x,y)
            lcd.show()
        if key == 'F':
            displayObject(bmaps['F'],x,y)
            lcd.show()
        if key == 'I':
            displayObject(bmaps['I'],x,y)
            lcd.show()
        if key == 'J':
            displayObject(bmaps['J'],x,y)
            lcd.show()
        if key == 'K':
            displayObject(bmaps['K'],x,y)
            lcd.show()                        
        if key == 'L':
            displayObject(bmaps['L'],x,y)
            lcd.show()
        if key == 'M':
            displayObject(bmaps['M'],x,y)
            lcd.show()
        if key == 'N':
            displayObject(bmaps['N'],x,y)
            lcd.show()
        if key == 'O':
            displayObject(bmaps['O'],x,y)
            lcd.show()
        if key == 'P':
            displayObject(bmaps['P'],x,y)
            lcd.show()
        if key == 'Q':
            displayObject(bmaps['Q'],x,y)
            lcd.show()
        if key == 'R':
            displayObject(bmaps['R'],x,y)
            lcd.show()
        if key == 'S':
            displayObject(bmaps['S'],x,y)
            lcd.show()
        if key == 'T':
            displayObject(bmaps['T'],x,y)
            lcd.show()
        if key == 'U':
            displayObject(bmaps['U'],x,y)
            lcd.show()
        if key == 'V':
            displayObject(bmaps['V'],x,y)
            lcd.show()
        if key == 'W':
            displayObject(bmaps['W'],x,y)
            lcd.show()
        if key == 'X':
            displayObject(bmaps['X'],x,y)
            lcd.show()                        
        if key == 'Y':
            displayObject(bmaps['Y'],x,y)
            lcd.show()
        if key == 'Z':
            displayObject(bmaps['Z'],x,y)
            lcd.show()
        if key == '[':
            displayObject(bmaps['['],x,y)
            lcd.show()
        # if key == '\':
        #     displayObject(bmaps['\'],x,y)
        #     lcd.show()
        if key == ']':
            displayObject(bmaps[']'],x,y)
            lcd.show()
        if key == '^':
            displayObject(bmaps['^'],x,y)
            lcd.show()
        if key == '_':
            displayObject(bmaps['_'],x,y)
            lcd.show()
        if key == '`':
            displayObject(bmaps['`'],x,y)
            lcd.show()
        if key == 'a':
            displayObject(bmaps['a'],x,y)
            lcd.show()
        if key == 'b':
            displayObject(bmaps['b'],x,y)
            lcd.show()
        if key == 'c':
            displayObject(bmaps['c'],x,y)
            lcd.show()
        if key == 'd':
            displayObject(bmaps['d'],x,y)
            lcd.show()
        if key == 'e':
            displayObject(bmaps['e'],x,y)
            lcd.show()                        
        if key == 'f':
            displayObject(bmaps['f'],x,y)
            lcd.show()
        if key == 'i':
            displayObject(bmaps['i'],x,y)
            lcd.show()
        if key == 'j':
            displayObject(bmaps['j'],x,y)
            lcd.show()
        if key == 'k':
            displayObject(bmaps['k'],x,y)
            lcd.show()
        if key == 'l':
            displayObject(bmaps['l'],x,y)
            lcd.show()
        if key == 'm':
            displayObject(bmaps['m'],x,y)
            lcd.show()
        if key == 'n':
            displayObject(bmaps['n'],x,y)
            lcd.show()
        if key == 'o':
            displayObject(bmaps['o'],x,y)
            lcd.show()
        if key == 'p':
            displayObject(bmaps['p'],x,y)
            lcd.show()
        if key == 'q':
            displayObject(bmaps['q'],x,y)
            lcd.show()
        if key == 'r':
            displayObject(bmaps['r'],x,y)
            lcd.show()
        if key == 's':
            displayObject(bmaps['s'],x,y)
            lcd.show()
        if key == 't':
            displayObject(bmaps['t'],x,y)
            lcd.show()                        

        if key == 'u':
            displayObject(bmaps['u'],x,y)
            lcd.show()
        if key == 'v':
            displayObject(bmaps['v'],x,y)
            lcd.show()   
        if key == 'w':
            displayObject(bmaps['w'],x,y)
            lcd.show()
        if key == 'x':
            displayObject(bmaps['x'],x,y)
            lcd.show()   
        if key == 'y':
            displayObject(bmaps['y'],x,y)
            lcd.show()
        if key == 'z':
            displayObject(bmaps['z'],x,y)
            lcd.show()   
        if key == '{':
            displayObject(bmaps['{'],x,y)
            lcd.show()
        if key == '|':
            displayObject(bmaps['|'],x,y)
            lcd.show()   
        if key == '}':
            displayObject(bmaps['}'],x,y)
            lcd.show()
        if key == '~':
            displayObject(bmaps['~'],x,y)
            lcd.show()   
      
        if key == 'q': #quit or start
            lcd.clear()
            lcd.show()


etchSketch(10,30)


