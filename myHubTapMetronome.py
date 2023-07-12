import time
from ble_emmaUPDATED import *
from ble_MIDI import *
from hub import motion_sensor
from hub import sound
from hub import light_matrix


#def metronome():
motion_sensor.reset_tap_count()
curr_tap_count = motion_sensor.tap_count()
 
while not done():
    if button.pressed(button.POWER):
        while not button.pressed(button.POWER):
            if motion_sensor.tap_count() > curr_tap_count:
                sound.beep(1000, 10, 100)
                curr_tap_count = motion_sensor.tap_count()




