import time, datetime
from datetime import date
import os

#Found = False
#rline = " "
#today = date.today()
#print(date.today(), '\n')
#print(datetime.datetime.today(), '\n')
#print(datetime.datetime.today().weekday())



# Find the next day with a Candle Lighting time by finding today's day of the week and then adding 1 to it until a candle lighting time is found
#i = datetime.datetime.today().weekday()
#print(i)
#j = 0

# if i == 0: j = 4
# elif i == 1: j = 3
# elif i == 2: j = 2
#print(j)



# Find out if today has a Candle Lighting time
def findCandle():

    # Find today's date and create a list of the day, month and year converted to integers
    datelist = str(date.today())
    datelist = datelist.split('-')
    for a in range(3):
        datelist[a]=int(datelist[a])

    # Create variables based on today's date
    year = str(datelist[0])
    month = str(datelist[1])
    day = str(datelist[2])

    # Find the next day that has a candle lighting time
    Found = False
    while Found == False:
        cmd = '../hebcal/hebcal -cTO ' + month + ' ' + day + ' ' + year + ' > s.txt'
        os.system(cmd)
        fhandle = open('s.txt')
        for line in fhandle:
            if line.startswith('Candle'):
                Found = True
                fhandle.close()
                return line
        day = str(int(day)+1)

candleTime = findCandle()
print(candleTime)
candleTime = candleTime.split()
print(candleTime[2])

# GUI

import tkinter as tk

HEIGHT = 240
WIDTH = 320

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

button = tk.Button(root, text='Test Button')
button.pack()

root.mainloop()
