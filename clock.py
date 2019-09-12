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
    #print('start findCandle()')

    # Find today's date and create a list of the day, month and year converted to integers
    datelist = str(date.today())
    datelist = datelist.split('-')
    for a in range(3):
        datelist[a]=int(datelist[a])

    # Create variables based on today's date
    year = str(datelist[0])
    month = str(datelist[1])
    day = str(datelist[2])

    Found = False
    while Found == False:
        # print('Start While()')
        # print(day)
        cmd = '../hebcal/hebcal -cTO ' + month + ' ' + day + ' ' + year + ' > s.txt'
        os.system(cmd)
        fhandle = open('s.txt')
        for line in fhandle:
            if line.startswith('Candle'):
                Found = True
                fhandle.close()
                return line
        #     else:
        #         print('Found is ', Found, ' so do While() again')
        day = str(int(day)+1)
        #print('Day is now ', day)
        #     fhandle.close()

print(findCandle())

# fhandle = open('s.txt')
# for line in fhandle:
#     #line = line.rstrip()
#     if line.startswith('Candle'): Found = True
#     #     fhandle.close()
#     #     print(line)
#     # else:
#     #     fhandle.close()
#     #     day = str(int(day)+1)
#     #     findCandle()
#     #     fhandle = open('s.txt')
#     #t.append(line)
#     #print(t)
# fhandle.close()
#print('Found is ', Found)
#print('rline is: ', rline)
# if Found == False:
#     day = str(int(day)+1)
#     findCandle()
# else:
#     print(rline)


#print('Output: ', os.system(cmd))
#Shabbat = date.today() + j
#print('Shabbat will start on Friday, ', Shabbat)
