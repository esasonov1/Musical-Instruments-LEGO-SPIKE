import time
from ble_MIDI import *
from hub import *



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
        
                
def start():
    try:
        while not done():
            if not motion_sensor.is_stable():
                play_note(50)
            else:
                time.sleep(.5)

          
    except:
        pass                             
           
    print('disconnect')
    midi.disconnect()
      


start()




            
