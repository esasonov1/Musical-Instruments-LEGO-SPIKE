from ble_emmaREDO import *
from ble_MIDI import *

import color_sensor, color         
from hub import port

color_note_mapping = {"Red": 0, "Green": 0, "Blue": 0, "Magenta": 0,
        "Yellow": 0, "Orange": 0, "Azure": 0, "Black": 0, "White": 0 }

'''
color_mapping = {
    "Red": 9,
    "Green": 6,
    "Blue": 3,
    "Magenta": 1,
    "Yellow": 7,
    "Orange": 2,
    "Azure": 4,
    "Black": 0,
    "White": 10 
}
'''

def read_color_dectection(port):
    detected_color = color_sensor.color(port)
    if detected_color is not None:
        print(f"Detected color: {detected_color}")
        time.sleep(0.1)



def Color_Note(port, red=0, green=0, blue=0, magenta=0, yellow=0, 
    orange=0, azure=0, black=0, white=0):
    

    if color_sensor.color(port) is color.RED:
        color_note_mapping["Red"] = red  
        return red
        
    elif color_sensor.color(port) is color.GREEN:
        color_note_mapping["Green"] = green
        return green
        
    elif color_sensor.color(port) is color.BLUE:
        color_note_mapping["Blue"] = blue
        return blue
        
    elif color_sensor.color(port) is color.MAGENTA:
        color_note_mapping["Magenta"] = magenta
        return magenta
        
    elif color_sensor.color(port) is color.YELLOW:
        color_note_mapping["Yellow"] = yellow
        return yellow
        
    elif color_sensor.color(port) is color.ORANGE:
        color_note_mapping["Orange"] = orange
        return orange
                
    elif color_sensor.color(port) is color.AZURE:
        color_note_mapping["Azure"] = azure
        return azure

    elif color_sensor.color(port) is color.BLACK:
        color_note_mapping["Black"] = black
        return black
        
    elif color_sensor.color(port) is color.WHITE:
        color_note_mapping["White"] = white
        return white
        
        
    print(color_note_mapping)
    time.sleep(.5)
    
        
while True:        
    Color_Note(port.A, white=99)
