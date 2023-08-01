from ble_emmaREDO import *
from ble_MIDI import *


time.sleep(2)

#Happy Birthday LEGO
play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")
play_the_note(NoteToNumber("C",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("E",3), .5, "ffff")

play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")
play_the_note(NoteToNumber("C",3), .25, "ffff")
play_the_note(NoteToNumber("G",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .5, "ffff")

play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("C",4), .25, "ffff")
play_the_note(NoteToNumber("A",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("E",3), .25, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")

play_the_note(NoteToNumber("Bb",3), .1875, "ffff")
play_the_note(NoteToNumber("Bb",3), .0625, "ffff")

play_the_note(NoteToNumber("A",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("G",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .5, "ffff")
   
#disconnect()





























'''
while not done():
    if Force_Sensor_Activated(port.C) and Force_Sensor_Activated(port.B):
        play_note("Force S",NoteToNumber("E",3), .5, "ffff", port.C)
    
    elif Force_Sensor_Activated(port.B) and Force_Sensor_Activated(port.A):
        play_note("Force S",NoteToNumber("G",3), .5, "ffff", port.B)
    
    elif Force_Sensor_Activated(port.A) and Force_Sensor_Activated(port.C):
        play_note("Force S",NoteToNumber("C",4), .5, "ffff", port.A)    
    
    elif Force_Sensor_Activated(port.A):
        play_note("Force S",NoteToNumber("C",3), .5, "ffff", port.A)
    
    elif Force_Sensor_Activated(port.B):
        play_note("Force S",NoteToNumber("D",3), .5, "ffff", port.B)
    
    elif Force_Sensor_Activated(port.C):
        play_note("Force S",NoteToNumber("F",3), .5, "ffff", port.C)
    
    else:
        time.sleep(.5)
'''   
