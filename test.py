import button
import time
from ble_MIDI import *

notes = [79,74,71,79,74,71,79,74,77,74,69,77,74,69,77,74
         ,77,74,69,77,74,69,77,74,76,74,69,76,74,69,76,74]

done = lambda : button.button_pressed(button.BUTTON_RIGHT)
    
def Music():
    midi = MIDI_Player('emma')
    midi.wait_for_connection()
    Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'],channel = 0)
 
    try:
        while not done():
            for x in notes:
                Piano.on(x,velocity['f'])
                time.sleep(0.1)
                Piano.off(x)
                time.sleep(0.1)
    except:
        pass
        
    midi.disconnect()

Music()





