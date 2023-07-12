from ble_emmaUPDATED import *
from ble_MIDI import *


while not done():
    if Force_Sensor_Activated(port.D):
        play_note("Color S", 60, 1, 'ffff')
    else:
        time.sleep(.5)
    
#disconnect()
