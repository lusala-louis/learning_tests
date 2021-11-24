from time import *
from threading import Thread
def myBox(delayT):
    while True:
        print('My Box is Open')
        sleep(delayT)
        print('My Box is Closed')
        sleep(delayT)
def myLED(delayP):
    while True:
        print('My LED is On')
        sleep(delayP)
        print('My LED is Off')
        sleep(delayP)
boxDelay=5
LEDDelay=1
boxThread=Thread(target=myBox, args=(boxDelay,))
LEDthread=Thread(target=myLED, args=(LEDDelay,))
boxThread.daemon=True
LEDthread.daemon=True
boxThread.start()
LEDthread.start()
while True:
    pass