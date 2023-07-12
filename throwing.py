import button
import time
from ble_MIDI import *
import imu

notes = [60,61,62,63,64,63,62,61]

done = lambda : button.button_pressed(button.BUTTON_RIGHT)
    
def Music():
    midi = MIDI_Player('chris')
    midi.wait_for_connection()
    Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'],channel = 0)
    
    try:
        while not done():
            accel = imu.getAcceleration()[2]
            x = (1000 - accel)/10
            #x = x if x < 127 else 45
            Piano.on(x,velocity['ff'])
            time.sleep(0.5)
    except:
        pass
        
    midi.disconnect()

Music()


