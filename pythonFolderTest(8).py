from ble_emmaREDO import *
from ble_MIDI import *


while not done():
    if Force_Sensor_Activated(port.F):
        play_note("m", 1, .1, "ffff", port.E)
    else:
        time.sleep(.5)

    
disconnect()
