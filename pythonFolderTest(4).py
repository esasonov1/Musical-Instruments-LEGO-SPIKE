from ble_emmaPORTS import *
from ble_MIDI import *

while not done():
    if Force_Sensor_Activated(port.F):   
        play_note("Color S", NoteToNumber("Eb",3), .4, "ffff")
             
    else:
        print("Nothing")
        time.sleep(.25)




disconnect()

