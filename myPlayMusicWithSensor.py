import time
from ble_MIDI import *
from hub import *
import color_sensor

#plug in color sensor to port E
#plays notes when light sensor is activate


#notes for coldplays clocks
notes = [79,74,71,79,74,71,79,74,77,74,69,77,74,69,77,74
        ,77,74,69,77,74,69,77,74,76,74,69,76,74,69,76,74]

def done():
    return button.pressed(button.RIGHT)
       


def readlight():
    return color_sensor.reflection(port.E)

def sensor_activated():
    print('printing light value')
    print(readlight())
    time.sleep(1)
    return readlight() > 50



midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'],channel = 0)


while not done():
    print("here")
    if sensor_activated():
        for x in notes:
            Piano.on(x,velocity['f'])
            time.sleep(0.1)
            Piano.off(x)
            time.sleep(0.1)


midi.disconnect()
