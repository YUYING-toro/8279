import csv

girls
result = []
f=open('/home/pi/Documents/python/1127_PY_Lab10/2000_GirlsNames.txt','r')
for line in f:
    result.append(list(line.strip('\n').split(',') ))
    
with open('/home/pi/Documents/python/1127_PY_Lab10/2000_GirlsNames.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['First Name','Count'])
    w.writerows(result)

# boy
boyli=[]
boy_op = open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.txt','r') 
for line in boy_op:
    boyli.append(list(line.strip('\n').split(',') ))
with open('/home/pi/Documents/python/1127_PY_Lab10/2000_BoysNames.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['First Name','Count'])
    w.writerows(boyli)



f.close()
boy_op.close()
