import time, datetime
from datetime import date
import os

#today = date.today()
#print(date.today(), '\n')
#print(datetime.datetime.today(), '\n')
#print(datetime.datetime.today().weekday())

# Find today's date and create a list of the day, month and year converted to integers
datelist = str(date.today())
#print(datelist)
datelist = datelist.split('-')
for a in range(3):
    datelist[a]=int(datelist[a])
print(datelist)

# Find the next day with a Candle Lighting time by finding today's day of the week and then adding 1 to it until a candle lighting time is found
i = datetime.datetime.today().weekday()
#print(i)
#j = 0

# if i == 0: j = 4
# elif i == 1: j = 3
# elif i == 2: j = 2
#print(j)

year = str(datelist[0])
cmd = '../hebcal/hebcal -cTO ', year, ' > s.txt'
print(cmd)
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
