import sqlite3
conn = sqlite3.connect(
    "C:/Users/user/Desktop/CA/01AC/python/Lab/L11/week11.db")
con3 = conn.cursor()
# test = sqlite3.connect("C:\Users\user\Desktop\CA\01AC\python\Lab\L11\week11.db")
cursor = con3.execute('select link from lab10')
cu = cursor.fetchall()
for row in cu:
    print(row)
