import pyautogui as gui

import time

message = input("enter the message:")
number = input("enter the number: ")

time.sleep(2)

for i in range (int(number)):
    gui.typewrite(message)
    gui.press('enter')
