import sqlite3
import base64
import webbrowser

def readDB(n):
    conn = sqlite3.connect(
        "C:/Users/user/Desktop/CA/01AC/python/Lab/L11/week11.db")
    con3 = conn.cursor()
    cursor = con3.execute('select link from lab10 where id = ?',(n,))
    url = cursor.fetchall()
    return url

def de_64(n):
    s1 = readDB(n)
    che = s1[0][0]
    b1 = che.encode('UTF-8')
    d = base64.b64decode(b1)
    s2 = d.decode('UTF-8')
    webbrowser.open(s2)

def task2(m):
    isStr = ask.isnumeric()
    if isStr == True:
        int_ask = int(ask)
        if 1 <= int_ask <= 24:
            de_64(int_ask)
            yorn = False
        else:
            print('not in range')
            yorn = True
    else:
        print('NOT NUMBER')

yorn = True
while yorn:
    ask = input('give a Int number ? or press q to stop search ')
    if ask == 'q':
        yorn = False
    else:
        task2(ask)

ask2 = input('what city? ')
ask3 = input('what country? ')

conn = sqlite3.connect(        "C:/Users/user/Desktop/CA/01AC/python/Lab/L11/week11.db")
con3 = conn.cursor()
cursor = con3.execute('Update Lab10 set City=?, Country=? where id=?', (ask2, ask3, ask))

conn.close()
con3.close()

