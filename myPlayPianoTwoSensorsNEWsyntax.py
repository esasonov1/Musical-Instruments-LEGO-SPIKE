import time
from ble_MIDI import *
from hub import *
import distance_sensor as ds
import color_sensor 
import motor

def done():
    return button.pressed(button.RIGHT)
    

class Music:
    def __init__(self):
        self.midi = MIDI_Player('emma')
        self.midi.wait_for_connection()
        self.Piano = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0)
        self.old_note = -1
        
        
    def play_note(self, note):
        self.Piano.on(note, velocity['f'])
        time.sleep(.5)
        self.Piano.off(note)
        
    def play_chord(self, note1, note2):
        self.Piano.on([note1, note2], velocity['f'])
        time.sleep(.5)
        self.Piano.off()
                
    def get_note_from_distance(self, distance):
        if distance == -1 or distance > 500:
            return -1
        elif distance < 500:
            note1 = int(8 + (distance / 5))
            note2 = note1 - 5
            return note1, note2    

    def read_light(self):
        return color_sensor.reflection(port.C)

    def sensor_activated(self):
        return self.read_light() > 50
        
    def move_motor(self):
        p1 = port.A
        motor.run_for_degrees(p1, 360, 1000)
        time.sleep(0.01)
        motor.run_for_degrees(p1, -360, 1000)
        time.sleep(0.01)

    def start(self):
        try:
            while not done():
                
                distance = ds.distance(port.F)
                light_value = self.read_light()
                
                if self.sensor_activated() and distance != -1:
                    note1, note2 = self.get_note_from_distance(distance)
                    print("about to play chord")
                    print(note1, note2)
                    self.play_chord(note1, note2)
                    time.sleep(0.1)
                    
                elif distance != -1:
                    note1, note2 = self.get_note_from_distance(distance)
                  
                    if self.old_note != note1:
                        print(note1)
                        self.play_note(note1)
                        time.sleep(0.1)
                        self.old_note = note1
                        
                elif self.sensor_activated():
                    print("about to play light sensor note")
                    self.play_note(50)
                    time.sleep(0.1)
 
                else:
                    print('motor')
                    time.sleep(0.25)
                    motor.motor_move_by_degrees(port.A, 5, 1000)
                    time.sleep(0.25)
                
                
        except:
            pass
            
        print('disconnect')
        self.midi.disconnect()

                
music = Music()
music.start()
