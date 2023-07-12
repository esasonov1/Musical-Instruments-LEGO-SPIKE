import time
from ble_MIDI import *
import hub, utime, port
import color_sensor, display, sound, motor, button
import distance_sensor as ds

def done():
    return button.button_pressed(button.BUTTON_RIGHT)
    


class Music:
    def __init__(self):
        self.midi = MIDI_Player('emma')
        self.midi.wait_for_connection()
        self.Piano = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0)
        self.old_note = -1
        
    def play_note(self, note, duration=0.5):
        self.Piano.on(note, velocity['f'])
        time.sleep(duration)
        self.Piano.off(note)
                
    def get_note_from_distance(self, distance):
        if distance == -1 or distance > 500:
            return -1
        elif distance < 500:
            note = 120
            return note
        
        
    def start(self):
        try:
            while not done():
                distance = ds.get_distance(port.PORTF)
                   
                if distance != -1:
                    note = self.get_note_from_distance(distance)
                  
                    if self.old_note != note:
                        print(note)
                        self.play_note(note)
                        time.sleep(0.1)
                        self.old_note = note
        except:
            pass

        self.midi.disconnect()
        
music = Music()
while not done():
    music.start()