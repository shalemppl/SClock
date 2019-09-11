import time, datetime
from datetime import date
import os

#today = date.today()
#print(date.today(), '\n')
#print(datetime.datetime.today(), '\n')
#print(datetime.datetime.today().weekday())

i = datetime.datetime.today().weekday()
j = 0

if i == 0: j = 4
elif i == 1: j = 3
elif i == 2: j = 2
#print(j)

cmd = '../hebcal/hebcal -cTO 09 13 2019 > s.txt'
os.system(cmd)

fhandle = open('s.txt')
t = []
for line in fhandle:
    line = line.rstrip()
    #if line.startswith('Candle'): print(line)
    t.append(line)
    print(t)
fhandle.close()
#print('Output: ', os.system(cmd))
#Shabbat = date.today() + j
#print('Shabbat will start on Friday, ', Shabbat)
