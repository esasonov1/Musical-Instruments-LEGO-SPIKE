import time
from ble_MIDI import *
from hub import *
import motor


midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
            
        
def play_note(note):
    Piano.on(note, velocity['f'])
    #while activated():
        #time.sleep(.1)
    time.sleep(.01)    
    Piano.off(note)
    time.sleep(.05)
        
def activated():
    if force_sensor.force(port.C) > 0:
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
    try:
        while not done():
            motor.run_for_time(port.D, 1000, 280)
            if activated():
                activate_motor()
            else:
                motor.run_for_time(port.D, 1000, -280)
                time.sleep(.1)
                        
    except:
        pass                             
            
    print('disconnect')
    midi.disconnect()
        
        
#motor.run_to_absolute_position(port.D, 0, 1000)
start()
