# Write your code here :-)
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sleep(1000)
        display.clear()
        
        
    if button_b.is_pressed():
        display.show(Image.SAD)
        sleep(1000)
        display.clear()
        