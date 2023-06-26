from ble_emma import *
from ble_MIDI import *

def NoteToNumber(note, octave = 0):
    notes = {"C": 24,"Db": 25,"D": 26,"Eb": 27,"E": 28,"F": 29,"Gb": 30,"G": 31,"Ab": 32, "A": 33,"Bb": 34,"B": 35}
    
    try:  
        if octave > 8 or octave < 0:
            raise Exception("Invalid octave input")
        if note not in notes:
            raise Exception("Invalid note input")
    
        if(octave > 0):
            return((notes[note]) + (octave*12))
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False
    
    
   

while not done():
    if Force_Sensor_Activated:
        play_note("Force S",NoteToNumber("Eb", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("G", 3),.3)
        play_note("Force S",NoteToNumber("Eb", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("G", 3),.3) 
        play_note("Force S",NoteToNumber("Eb", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)    
                  
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)   
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)    
        play_note("Force S",NoteToNumber("Db", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)        
                  
        play_note("Force S",NoteToNumber("C", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)
        play_note("Force S",NoteToNumber("C", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        play_note("Force S",NoteToNumber("F", 3),.3)
        play_note("Force S",NoteToNumber("C", 4),.3)
        play_note("Force S",NoteToNumber("Bb", 3),.3)
        
        