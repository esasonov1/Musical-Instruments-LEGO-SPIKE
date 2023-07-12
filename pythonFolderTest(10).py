from ble_emmaUPDATED import *
from ble_MIDI import *


while not done():
    if Force_Sensor_Activated(port.A):
        play_note("Force S", 50, .2)

        
  
    else:
        time.sleep(.5)
   
   
   
#disconnect()
