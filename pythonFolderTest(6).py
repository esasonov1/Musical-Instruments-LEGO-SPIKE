from ble_emmaREDO import *
from ble_MIDI import *


while not done():
    if Force_Sensor_Activated(port.D):
        play_note("Distance S", 60, 1, 'ffff',port.F)
    if Color_Sensor_Activated(port.C):
        play_note("Color S", 70, 1, 'ffff', port.C)
        

disconnect()
