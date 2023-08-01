from ble_emmaREDO import *
from ble_MIDI import *


while not done():
    if Color_Sensor_Activated(port.A):
        play_note("Color S", 60, 1, 'ffff', port.A)
    else:
        time.sleep(.5)
    
#disconnect()
