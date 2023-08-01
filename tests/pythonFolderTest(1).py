from ble_emma import *
from ble_MIDI import *


test()


while not done():
    #play_note("N", "Side Stick", .25)
    
    if Force_Sensor_Activated():   
        play_note("Force S", "Low Tom", .25)
    elif Color_Sensor_Activated():
        play_note("Color S", "Closed Hi-Hat", .25)
    else:
        print("else")
        time.sleep(.25)
        play_note("N", "Hand Clap", .25)



disconnect()
