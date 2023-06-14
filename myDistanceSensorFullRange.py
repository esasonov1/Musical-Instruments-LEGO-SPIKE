import time
from ble_MIDI import *
from hub import *
import distance_sensor as ds


#Plug in Distance Sensor to port F
#use distance sensor to play a range of notes
#right button on hub disconnects


midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
       
        
def play_note(note):
    Piano.on(note, velocity['f'])
    time.sleep(.1)
    Piano.off(note)
    time.sleep(.1)
        
                
def get_note_from_distance(dist):
    if dist == -1 or dist > 500:
        return -1
    elif dist < 500:
        note = int(8 + (dist / 5))
        return note
        
def start():
    try:
        while not done():
            dist = ds.distance(port.F)
            print(dist)
            time.sleep(.1)
                
            if dist != -1:
                note = get_note_from_distance(dist)
                play_note(note)                 

    except:
        pass                             
           
    print('disconnect')
    midi.disconnect()
              
start()


