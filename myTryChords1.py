import time
from ble_MIDI import *
from hub import *
import force_sensor

#notes = [60,61,62,63,64,63,62,61]
notes = [60, 64, 67]

def done(): 
    return button.pressed(button.RIGHT)
       
  
midi = MIDI_Player('chris')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'],channel = 0)
Trumpet = MIDI_Instrument(midi, instruments['Trumpet'],channel = 1)

while not done():
    Piano.on(chord(notes),velocity['ff'])
    time.sleep(.5)
    Piano.off(chord(notes),velocity['ff'])
   
    

midi.disconnect()


