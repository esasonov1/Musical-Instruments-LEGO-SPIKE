import time
from ble_MIDI import *
from hub import *
import distance_sensor as ds
import force_sensor


#Plug in Distance Sensor to port F and Force Sensor to port A
#use distance sensor to play a range of notes with the force sensor
#right button on hub disconnects


def done(): 
    return button.pressed(button.RIGHT)
        
        
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


def fs_activated():
    if force_sensor.force(port.A) > 0:
        return True
    else:
        return False

        
def start():

    while not done():
        dist = ds.distance(port.F)
        
        if(fs_activated()):
            
            print(dist)
            time.sleep(.1)
                
            if dist != -1:
                note = get_note_from_distance(dist)
                play_note(note)    
                
        else: 
            time.sleep(.1)
            print("Force Sensor NOT activated!")           
    
                        
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
            
        
start()

print('disconnect')
midi.disconnect()
