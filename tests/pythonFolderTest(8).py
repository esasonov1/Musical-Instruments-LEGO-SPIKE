from ble_emmaREDO import *
from ble_MIDI import *
#test()


while True:
    #play_note("Color S", 62, 1, 'fff', port.E)
    play_note("Color S", 66, 1, 'fff', port.C)
    play_note("Color S", 69, 1, 'fff', port.A)


disconnect()
