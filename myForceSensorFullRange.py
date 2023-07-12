import time
from ble_MIDI import *
from hub import *
import force_sensor

#Plug in Force Sensor to port C
#push force button to play a range of notes
#right button on hub disconnects
        

def done(): 
    return button.pressed(button.RIGHT)
        
        
def play_note(note):
    Piano.on(note, velocity['f'])
    time.sleep(.1)
    Piano.off(note)
    time.sleep(.1)
        
                
def start():
    try:
        while not done():
            fs = force_sensor.force(port.C)
            print(fs)
            
            note_range = 108 - 21  # Total number of notes in the range
            note_value = int((fs / 100) * note_range) + 21  # Map the force sensor value to the note range

            play_note(note_value)
                        
    except:
        pass                             
            
    print('disconnect')
    midi.disconnect()

        
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)

        
start()
