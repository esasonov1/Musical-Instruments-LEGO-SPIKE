wimport time
from ble_MIDI import *
from hub import *
import motor
import device
import force_sensor



deviceTypeLookup={48:'m',49:'M',61:'Color S',62:'Distance S',63:'Force S',255:'N'}
deviceType=[0]*6

def ReadPorts():
    for i in range(6):
        deviceType[i] = deviceTypeLookup[device.device_id(i)]
        
        
def done(): 
    return button.pressed(button.RIGHT)
            
        
def play_note(note):
    Piano.on(note, velocity['f'])
    while activated():
        time.sleep(.1)
        
    Piano.off(note)
    time.sleep(.1)
        
def activated():
    if force_sensor.force(forceS_loc) > 0:
        return True
    else:
        return False

def activate_motor():
    mpos = motor.absolute_position(motor_loc)
            
    if mpos < 0:
        mpos = mpos + 360  
                
    print(mpos)
    note_range = 108 - 21  #Total number of notes in the range
    note_value = int((mpos / 360) * note_range) + 21  #Maps the notes and value
    play_note(note_value)
        
                
def start():
    try:
        while not done():
            if activated():
                activate_motor()
            else:
                time.sleep(.1)
                        
    except:
        pass                             
            
    print('disconnect')
    midi.disconnect()

        
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)

        
start()
