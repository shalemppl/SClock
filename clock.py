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

def testfx():
    print('Click')

HEIGHT = 240
WIDTH = 320

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

bgImage = tk.PhotoImage(file='bgImage.gif')
bgLabel = tk.Label(root, image=bgImage)
bgLabel.place(relwidth=1, relheight=1)

# frame = tk.Frame(root)
# frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1, anchor='w')

# button = tk.Button(root, text=candleTime[2], command=testfx)
# button.place(relx=0.1, relheight=0.3, relwidth=0.3)

# candleTimeFrame = tk.Frame(root)
# candleTimeFrame.place(relx=0.5, rely=0.25, relwidth=0.25, relheight=0.1, anchor='n')

candleTimeLabel = tk.Label(root)
candleTimeLabel.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)
candleTimeLabel['text'] = candleTime[2] + ' PM'

root.mainloop()
