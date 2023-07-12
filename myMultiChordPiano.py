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
        self.Piano1 = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0)
        self.Piano2 = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=1)
        self.old_note1 = -1
        self.old_note2 = -1
        
    def play_notes(self, note1, note2, duration=0.5):
        self.Piano1.on(note1, velocity['f'])
        self.Piano2.on(note2, velocity['f'])
        time.sleep(duration)
        self.Piano1.off(note1)
        self.Piano2.off(note2)
                
    def get_note_from_distance(self, distance):
        if distance == -1 or distance > 500:
            return -1, -1
        elif distance < 500:
            note1 = int(8 + (distance / 5))
            note2 = note1 + 5
            return note1, note2
        
    def start(self):
        try:
            while not done():
                distance = ds.get_distance(port.PORTF)
                
                if distance != -1:
                    note1, note2 = self.get_note_from_distance(distance)
                  
                    if self.old_note1 != note1 or self.old_note2 != note2:
                        print(note1, note2)
                        self.play_notes(note1, note2)
                        time.sleep(0.1)
                        self.old_note1 = note1
                        self.old_note2 = note2
        except:
            pass

        self.midi.disconnect()
        
music = Music()
while not done():
    music.start()