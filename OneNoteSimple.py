from ble_emmaREDO import *
from ble_MIDI import *


while not done():
    
    if Force_Sensor_Activated(port.A):
        play_note("Force S", "Low Tom", .2, "ffff", port.A)
    
    elif Color_Sensor_Activated(port.B):
        play_note("Color S","Pedal Hi-Hat", .2, "ffff", port.B)
    
    elif Color_Sensor_Activated(port.C):
        play_note
        
    
        
    