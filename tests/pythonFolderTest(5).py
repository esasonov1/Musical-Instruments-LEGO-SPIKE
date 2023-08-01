from ble_emmaPORTS import *
from ble_MIDI import *

while not done():
    if Distance_Sensor_Activated(port.E):   
        play_note("Distance S", 70, .4, "ffff")
             
    else:
        print("Nothing")
        time.sleep(.25)




disconnect()

