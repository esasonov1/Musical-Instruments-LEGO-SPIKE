from ble_emmaPORTS import *
from ble_MIDI import *


test()


while not done():
    if Force_Sensor_Activated(port.A):   
        play_note("Force S", "Low Tom", .25, "ffff", port.A)
        
    elif Force_Sensor_Activated(port.C):   
        play_note("Force S", "High Tom", .25, "ffff", port.C)
        
    elif Force_Sensor_Activated(port.E):   
        play_note("Force S", "Rim Shot", .25, "ffff", port.E)
        
    elif Color_Sensor_Activated(port.B):
        play_note("Color S", "Crash Cymbal", 1, "p", port.B)
        
    elif Color_Sensor_Activated(port.D):
        play_note("Color S", "Closed Hi-Hat", .25, "ffff", port.D)
        
    elif Color_Sensor_Activated(port.F):
        play_note("Color S", "Hand Clap", .25,"pp", port.F)
        
    else:
        print("Nothing")
        time.sleep(.25)




#disconnect()
