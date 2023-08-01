from ble_emmaREDO import *
#from ble_MIDI import *


while not done():
    
    if Color_Sensor_Activated(port.A) and Color_Sensor_Activated(port.C):
        play_note("Color S", [NoteToNumber("C",4), NoteToNumber("E",4),NoteToNumber("G",4)], 1, "ffff", port.A)
    
    elif Color_Sensor_Activated(port.C) and Color_Sensor_Activated(port.E):
        play_note("Color S", [NoteToNumber("E",4), NoteToNumber("G",4)], 1, "ffff", port.C)
    
    elif Color_Sensor_Activated(port.E) and Color_Sensor_Activated(port.A):
        play_note("Color S", [NoteToNumber("G",4), NoteToNumber("C",4)], 1, "ffff", port.E)
            
        
    if Color_Sensor_Activated(port.A):
        play_note("Color S", NoteToNumber("C",4), 1, "ffff", port.A)
        
    elif Color_Sensor_Activated(port.C):
        play_note("Color S", NoteToNumber("E",4), 1, "ffff", port.C)
        
    elif Color_Sensor_Activated(port.E):
        play_note("Color S", NoteToNumber("G",4), 1, "ffff", port.E)       
        

    
    
'''    
    if Color_Sensor_Activated(port.A) and Color_Sensor_Activated(port.C):
        play_note("Color S", [NoteToNumber("C",4), NoteToNumber("E",4)], 1, "ffff", port.A)
    
    elif Color_Sensor_Activated(port.C) and Color_Sensor_Activated(port.E):
        play_note("Color S", [NoteToNumber("E",4), NoteToNumber("G",4)], 1, "ffff", port.C)
    
    elif Color_Sensor_Activated(port.E) and Color_Sensor_Activated(port.A):
        play_note("Color S", [NoteToNumber("G",4), NoteToNumber("C",4)], 1, "ffff", port.E)
            
        
    elif Color_Sensor_Activated(port.A):
        play_note("Color S", NoteToNumber("C",4), 1, "ffff", port.A)
        
    elif Color_Sensor_Activated(port.C):
        play_note("Color S", NoteToNumber("E",4), 1, "ffff", port.C)
        
    elif Color_Sensor_Activated(port.E):
        play_note("Color S", NoteToNumber("G",4), 1, "ffff", port.E)       
'''        

        
#disconnect()
