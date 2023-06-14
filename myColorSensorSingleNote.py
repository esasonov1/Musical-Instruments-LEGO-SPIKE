import time
from ble_MIDI import *
from hub import *
import color_sensor


#Plug in Color Sensor to port E
#cover the light to activate a single note
#right button on hub disconnects

midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
    

def done(): 
    return button.pressed(button.RIGHT)
       

def play_note(note):
    Piano.on(note, velocity['f'])
    time.sleep(0.1)
    Piano.off(note)
    time.sleep(0.1)
            

def read_light():
        return color_sensor.reflection(port.E)

def activated():
        return read_light() > 50

                
def start():
    try:
        while not done():
            if activated(): 
                print(color_sensor.reflection(port.E))
                play_note(50)
            else:
                time.sleep(.1)
                          
    except:
        pass                             
           
    print('disconnect')
    midi.disconnect()
      
        
start()


            
