from hub import *
import time


def playNoise(pos):
    if pos==0:
        speaker.beep(500,100,100)
        time.sleep_ms(100)
        speaker.beep(600,100,100)
        time.sleep_ms(100)
        speaker.beep(600,100,100)
        time.sleep_ms(100)
    else:
        speaker.beep(pos*100+300, 300, 100)
        time.sleep_ms(300)

pos = 0

while True:
    if button.pressed(button.RIGHT):
        pos =(pos+1)%5
        playNoise(pos)
    elif button.pressed(button.LEFT):
        pos = (pos-1)%5
        playNoise(pos)
    elif buttom.pressed(button.POWER):
        # execute code stored in current pos
    else:
        time.sleep_ms(10)
