import time
from ble_MIDI import *
from hub import *
import color_sensor
import distance_sensor as ds

def done(): #right button stops everything
    return button.pressed(button.RIGHT)

class Music:
    def __init__(self):
        self.midi = MIDI_Player('LEGO Instrument')#the name on the ipad in garage band, so its the name of the midi player
        self.midi.wait_for_connection() #only move when connected to garage band
        self.Piano = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0) #chooses garage band instrument, channels maybe can do multiple instruments with dif sensors?
        self.old_note = -1
        
    def read_light(self): #geting light sensor value
        return color_sensor.reflection(port.C)
        
    def play_note(self, note):
        self.Piano.on(note, velocity['f'])
        time.sleep(.5)
        self.Piano.off(note)
        
    def sensor_activated(self): #if close to sensor sensor is "on", prevents it from constantly making noise when nothing is near it
        return self.read_light() > 50
    
    
music = Music()   
        
while not done(): 
    
    print(music.read_light())
    time.sleep(.5)
    
    if music.sensor_activated():
        print("about to play light sensor note")
        music.play_note()
        time.sleep(0.1)

