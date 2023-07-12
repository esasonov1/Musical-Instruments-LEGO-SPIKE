import button
import time
from ble_MIDI import *
import hub, utime, port
import color_sensor, display, sound, motor, button

notes = [79,74,71,79,74,71,79,74,77,74,69,77,74,69,77,74
        ,77,74,69,77,74,69,77,74,76,74,69,76,74,69,76,74]

def done():
    return button.button_pressed(button.BUTTON_RIGHT)
    
#sensor = port.PORTC
    
class MusicPlayer:
    def __init__(self, midi_name: str, instrument: int, channel: int = 0):
        self.midi = MIDI_Player(midi_name)
        self.midi.wait_for_connection()
        self.instrument = instrument
        self.channel = channel
        self.piano = MIDI_Instrument(self.midi, self.instrument, channel=self.channel)
        self.note_index = 0
        
    def play_notes(self, notes: List[int], duration: float = 0.1):
        try:
            piano = MIDI_Instrument(self.midi, self.instrument, channel=self.channel)
            piano.on(notes[self.note_index], velocity['f'])
            time.sleep(duration)
            piano.off(notes[self.note_index])
            self.note_index = (self.note_index + 1) % len(notes) 
        except:
            pass
            

        
    def disconnect(self):
        self.midi.disconnect()


class sensor():
    def __init__(self, lightPort):
        self.lightPort = lightPort

    def readlight(self):
        return color_sensor.get_reflection(self.lightPort)

    def sensor_activated(self):
        return self.readlight() > 50
    
    
    
s = sensor(port.PORTC)
player = MusicPlayer('emma', instruments['Acoustic Grand Piano'])


while True:
    if s.sensor_activated():
        player.play_notes(notes)
        time.sleep(.2)
    if done():
        break
        
player.disconnect()
print("disconnected")
