import time
from ble_MIDI import *
from hub import *
import force_sensor

#Plug in Force Sensor to port C
#push force button to play a single note BUT the harder you push, the louder the sound
#right button on hub disconnects

midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
       

def velocity():
    velocity_range = 127
    velocity_value = int((force_sensor.force(port.C) / 100) * velocity_range)

    return velocity_value

def play_note(note):
    vel = velocity()
    Piano.on(note, vel)
    time.sleep(0.1)
    Piano.off(note)
    time.sleep(0.1)
            

def activated():
    if force_sensor.force(port.C) > 0:
        return True
    else:
        return False

                
def start():
    try:
        while not done():
            if activated(): 
                print(force_sensor.force(port.C))
                play_note(48)
            else:
                time.sleep(.1)
                          
    except:
        pass                             
           
    print('disconnect')
    midi.disconnect()
      
        
start()


            
