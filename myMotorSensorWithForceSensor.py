import time
from ble_MIDI import *
from hub import *
import motor
import force_sensor

#Plug in Force Sensor to port A and Motor to port D
#push force button and adjust music to play a range of notes
#right button on hub disconnects

def done(): 
    return button.pressed(button.RIGHT)
            
        
def play_note(note):
    Piano.on(note, velocity['f'])
    while activated():
        time.sleep(.1)
        
    Piano.off(note)
    time.sleep(.1)
        
def activated():
    if force_sensor.force(port.A) > 0:
        return True
    else:
        return False

def activate_motor():
    mpos = motor.absolute_position(port.D)
            
    if mpos < 0:
        mpos = mpos + 360  
                
    print(mpos)
    note_range = 108 - 21  #Total number of notes in the range
    note_value = int((mpos / 360) * note_range) + 21  #Maps the notes and value
    play_note(note_value)
        
                
def start():

    while not done():
        if activated():
            activate_motor()
        else:
            time.sleep(.1)

    
    
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)    
        
motor.run_to_absolute_position(port.D, 0, 1000)
start()

            
print('disconnect')
midi.disconnect()
