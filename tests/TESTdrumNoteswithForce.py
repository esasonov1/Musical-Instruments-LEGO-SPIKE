from ble_emma import *
from ble_MIDI import *



test()

i = 30

while not done():
    if Color_Sensor_Activated():
        play_note("Color S", i , 1,"pp")
        print(i)
    if Force_Sensor_Activated():
        play_note("Force S", i , .5, "ffff")
    if Color_Sensor_Activated() and Force_Sensor_Activated():    
        i+=1
        if i > 108:
            i = 30
        