from csv import reader
# import csv
# import Lab10_1
# import pandas as pd
# Write a python program that ''prompts'' the user for the name of .csv file 
# then reads and displays each line of thefile as a Python list. 
# Test your program on the 2 csv files that you generated in Task 1. 
# 家資料進

ask_g = input('what is your name,girl?')
ask_gli=[ask_g]

with open('/home/pi/Documents/python/1127_PY_Lab10/2000_GirlsNames.csv','r') as girl01:
    readerr = reader(girl01)
    # print(readerr)
    list_of_row =list(readerr) 
    list_of_row.append(ask_gli)
    print(list_of_row) # done to add new name
girl01.close()

ask_b = input('what is your name,boy?')
ask_bli=[ask_b]

with open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.csv','r') as boy01:
    readerB = reader(boy01)
    # print(readerr)
    list_of_rowB =list(readerB) 
    list_of_rowB.append(ask_bli)
    print(list_of_rowB) # done to add new name
boy01.close()



# print(ask_li)
# op = open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.csv','a')
#     # writer = csv.writer(toro)
# tryy = writer.write(ask_li) # no write
# print(tryy)


# def addG(ask_li):
#     with open('/home/pi/Documents/python/1127_PY_Lab10/200wit0_BoysNames.csv','a+',newline='') as ff:
#     append_list_as_roow()
    
# with open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.csv','r') as f:
#     w = f.readline(f)
#     print(w)
# girl_op=open('/home/pi/Documents/python/1127_PY_Lab10/2000_GirlsNames.csv','a')
#     writer = csv.writer(f)
#     writer.writerow(('ColA', 'ColB'))

# aaa=re_G.write(askG)
# print(aaa)

# open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.csv','w')

# file = open('sample.csv','a')
# file.write('orange,3')
# file.close()


# girl_op.close()