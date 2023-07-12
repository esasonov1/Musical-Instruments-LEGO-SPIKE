import time
from ble_MIDI import *
from hub import *
import distance_sensor as ds

def done(): #right button stops everything
    return button.button_pressed(button.BUTTON_RIGHT)
    
class Music:
    def __init__(self):
        self.midi = MIDI_Player('LEGO Instrument')#the name on the ipad in garage band, so its the name of the midi player
        self.midi.wait_for_connection() #only move when connected to garage band
        self.Piano = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0) #chooses garage band instrument, channels maybe can do multiple instruments with dif sensors?
        self.old_note = -1
        
    def play_note(self, note): #plays note for .5 seconds
        self.Piano.on(note, velocity['f'])
        time.sleep(.5)
        self.Piano.off(note)
        
    def play_chord(self, note1, note2): #plays two notes for .5 seconds
        self.Piano.on([note1, note2], velocity['f'])
        time.sleep(.5)
        self.Piano.off()
        
    def get_note_from_distance(self, distance): #ultrasonic sensor
        if distance == -1 or distance > 500:
            return -1
        elif distance < 500:
            note1 = int(8 + (distance / 5)) #this is just played around with, maybe a standardized way to do things?
            note2 = note1 - 5
            return note1, note2
            
    def read_light(self): #geting light sensor value
        return color_sensor.reflection(port.C)
        
    def sensor_activated(self): #if close to sensor sensor is "on", prevents it from constantly making noise when nothing is near it
        return self.read_light() > 50
        
    def move_motor(self): #moves the motor little by little
        p1 = port.PORTA
        motor.motor_move_by_degrees(p1, 360, 1000) #port, angle, speed or power
        time.sleep(0.01)
        motor.motor_move_by_degrees(p1, -360, 1000)
        time.sleep(0.01)
        
    def start(self):
        try:
            while not done():
                print(self.read_light())
                time.sleep(0.1)
                
                if self.sensor_activated():
                    print("about to play light sensor note")
                    self.play_note()
                    time.sleep(0.1)
        except:
            pass
            
        print('disconnect')
        self.midi.disconnect()
        
music = Music()
music.start()

