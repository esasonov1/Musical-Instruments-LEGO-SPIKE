#from ble_emmaPORTS import *
from ble_emmaPORTSmotorUPDATED import *
from ble_MIDI import *

while not done():
    if Force_Sensor_Activated(port.F):   
        play_note("Force S", NoteToNumber("Eb",3), .4, "ffff", port.F)
        
    elif Force_Sensor_Activated(port.D):   
        play_note("Force S", NoteToNumber("Db",3), .4, "ffff", port.D)
        
    elif Force_Sensor_Activated(port.B):   
        play_note("Force S", NoteToNumber("Bb",2), .4, "ffff", port.B)
        
    elif Color_Sensor_Activated(port.A):
        play_note("Color S", NoteToNumber("F",2), .4, "fff", port.A)
        
    elif Color_Sensor_Activated(port.C):
        play_note("Color S", NoteToNumber("G",2), .4, "ffff", port.C)
        
    elif Color_Sensor_Activated(port.E):
        play_note("Color S", NoteToNumber("C",3), .4,"fff", port.E)
               
    else:
        print("Nothing")
        time.sleep(.25)
        

disconnect()
