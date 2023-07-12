import time
from ble_MIDI import *
from hub import *
import motor


midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
        
        
def play_note(note):
    Piano.on(note, velocity['f'])
    time.sleep(.5)
    Piano.off(note)
    print(note)
        
                
def start():
    try:
        while not done():
            mpos = motor.absolute_position(port.A)
            
            if mpos < 0:
                mpos = mpos + 360  
                
            print(mpos)
                
            note_range = 108 - 21  #Total number of notes in the range
            note_value = int((mpos / 360) * note_range) + 21  #Maps the notes and value

            play_note(note_value)  
                    
    except:
        pass                             
            
    print('disconnect')
    midi.disconnect()
        
motor.run_to_absolute_position(port.A, 306, 1000)
start()
