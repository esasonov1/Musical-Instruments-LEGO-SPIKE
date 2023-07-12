from ble_emma import *
from ble_MIDI import *

#dynamics = {'off':0, 'pppp':8,'ppp':20,'pp':31,'p':42,'mp':53,'mf':64,'f':80,'ff':96,'fff':112,'ffff':127}

play_chord(NoteToNumber("C",6),NoteToNumber("E",6),NoteToNumber("G",6),NoteToNumber("C",7))
play_chord(NoteToNumber("C",5),NoteToNumber("E",5),NoteToNumber("G",5),NoteToNumber("C",6))
play_chord(NoteToNumber("C",4),NoteToNumber("E",4),NoteToNumber("G",4),NoteToNumber("C",5))
play_chord(NoteToNumber("C",3),NoteToNumber("E",3),NoteToNumber("G",3),NoteToNumber("C",4))
play_chord(NoteToNumber("C",2),NoteToNumber("E",2),NoteToNumber("G",2),NoteToNumber("C",3))
play_chord(NoteToNumber("C",3),NoteToNumber("Eb",3),NoteToNumber("G",3))
play_chord(NoteToNumber("C",2),NoteToNumber("Eb",2),NoteToNumber("G",2))
play_chord(NoteToNumber("C",1),NoteToNumber("Eb",1),NoteToNumber("G",1))


test()

first_notes = [63,58,55]
second_notes = [61,53,60]
third_notes = [61,53,60]
'''
while not done():
    if Force_Sensor_Activated():
        play_note("Force S", drumNotes['Snare Drum'], .4)
        play_note("Force S", drumNotes['Snare Drum'], .4)
        play_note("Force S", drumNotes['Crash Cymbal'], .75)
        #play_note("Force S", drumNotes['Hand Clap'], .5)
'''

'''
while not done():
    for i in range (3):
        play_note("Force S",first_notes[i],.5)
    for i in range (3):
        play_note("Force S",second_notes[i],2)
    for i in range (3):
        play_note("Force S",third_notes[i],2)
'''

while not done():
    if Color_Sensor_Activated():
        play_note("Color S", 75, 1, 'ffff')

    
disconnect()