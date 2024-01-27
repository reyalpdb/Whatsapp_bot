import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position()  #always true // postion of our mouse pointer
    print( posXY , pt.pixel(posXY[0], posXY[1]))
    sleep(1)  # delaying 1 sec
    if posXY[0] == 0:
        break