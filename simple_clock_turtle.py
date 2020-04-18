#This is a simple clock that is written using the turtle and the time module


import time
hours = 8
minutes = 32
seconds = 00

from turtle import *
#setup()
t1 = Turtle()

while True:
    t1.clear()
    #t1.clear - clears the screen after every write action
    
    t1.write(str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2),font=("arial",30,"normal"))
    #t1.write -- writes to the turtle window 
    #using zfill forces python to display two digits
    seconds = seconds+1
    time.sleep(1)
    #using time.sleep module we get the clock to move 1 sec
    if seconds == 60: #checks if seconds is sixty and increments mins
        seconds = 0
        minutes = minutes+1

    if minutes == 60: #checks if minutes is sixty and increments mins
        minutes = 0
        hours = hours +1
        
