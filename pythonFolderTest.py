from ble_emmaREDO import *
from ble_MIDI import *


test()


while not done():
    if Force_Sensor_Activated(port.A):
        play_note("Force S", "High Tom", .5, "ffff", port.A)
    elif Force_Sensor_Activated(port.B):
        play_note("Force S", "Low Tom", .5, "ffff", port.B)
    elif Force_Sensor_Activated(port.C):
        play_note("Force S", "Closed Hi-Hat", .5, "ffff", port.C)
    elif Force_Sensor_Activated(port.D):
        play_note("Force S", "Crash Cymbal", .5, "ffff", port.D)
    else:
        time.sleep(.01)

    
   
#disconnect()
