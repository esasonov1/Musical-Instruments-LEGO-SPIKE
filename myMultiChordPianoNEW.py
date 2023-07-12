import time
from ble_MIDI import *
from hub import *
import distance_sensor as ds


def done():
    return button.button_pressed(button.BUTTON_RIGHT)
    

class Music:
    def __init__(self):
        self.midi = MIDI_Player('emma')
        self.midi.wait_for_connection()
        self.Piano1 = MIDI_Instrument(self.midi, instruments['Acoustic Grand Piano'], channel=0)
        self.old_note1 = -1
        self.old_note2 = -1
        self.old_note3 = -1
        
    def play_notes(self, note1, note2, note3):
        self.Piano1.on([note1, note2, note3], velocity['f'])
        time.sleep(.5)
        self.Piano1.off()

                
    def get_note_from_distance(self, distance):
        if distance == -1 or distance > 500:
            return -1, -1
        elif distance < 500:
            note1 = int(8 + (distance / 5))
            note2 = note1 - 3
            note3 = note2 - 2
            return note1, note2, note3
        
    def start(self):
        try:
            while not done():
                distance = ds.get_distance(port.PORTF)
                
                if distance != -1:
                    note1, note2, note3 = self.get_note_from_distance(distance)
                  
                    if self.old_note1 != note1:
                        print(note1, note2, note3)
                        self.play_notes(note1, note2, note3)
                        time.sleep(0.1)
                        self.old_note1 = note1
                        self.old_note2 = note2
                        self.old_note3 = note3
        except:
            pass
        print('disconnect')
        self.midi.disconnect()
        
        
music = Music()
music.start()