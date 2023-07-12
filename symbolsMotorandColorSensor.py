import time
from ble_MIDI import *
from hub import *
import motor

#Plug in Force Sensor to port A and Motor to port D
#push force button and adjust music to play a range of notes
#right button on hub disconnects

midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
            
        
def play_note(note):
    Piano.on(note, velocity['f'])
    time.sleep(.5)    
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
    
def motor_activated():     
    if motor.absolute_position(port.C) > 170:
         return True
     else: 
         return False   
            
def start():
    try:
        while not done():
            if motor_activated():
                play_note(57)
            else:
                time.sleep(.1)
                
          
                        
    except:
        pass                             
            
    print('disconnect')
    midi.disconnect()
        
        
#motor.run_to_absolute_position(port.D, 0, 1000)
start()
