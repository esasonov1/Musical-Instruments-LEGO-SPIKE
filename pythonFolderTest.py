from ble_emmaONE import *
from ble_MIDI import *


test()

'''
while not done():
    play_note("Color S", 50, 1)
    time.sleep(1)

'''

while True:
    if Color_Sensor_Activated():    
        play_note("Color S", 50, 1)
    else:
        time.sleep(1)
        
    if Color_Sensor_Activated():    
        play_note("Color S", 60, 1)


disconnect()
