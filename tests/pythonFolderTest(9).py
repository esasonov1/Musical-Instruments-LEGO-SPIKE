from ble_emmaUPDATED import *
from ble_MIDI import *

dynamics = ["ppp", "pp", "p", "f", "ff", "fff", "ffff"]
i = 0

while not done():
    if Distance_Sensor_Activated(port.A):
        if i > 6:
            i = 0
        
        print(dynamics[i])
        play_note("Distance S", 100, .5, dynamics[i], port.A)
        i+=1
        
    else:
        time.sleep(.5)
   
   
   
#disconnect()
