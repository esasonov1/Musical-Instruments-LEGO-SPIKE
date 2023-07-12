from ble_MIDI import *
from hub import *
import motor
import runloop

symbol1 = {"start": 150, "stop": 180, "play": 175, "port": port.C, "speed":100, "name":"symbol 1"}
drum1 = {"start": 150, "stop": 180, "play": 175, "port": port.D, "speed":100, "name":"drum 1"}

drums = [symbol1]

async def drum1(drums):
    while True:
        for drum in drums:
            
            await motor.run_to_absolute_position(drum["port"],drum["start"],drum["speed"])
            await motor.run_to_absolute_position(drum["port"],drum["stop"],drum["speed"])


async def readPos(drums):
    drumplay = [False]*len(drums)
    while True:
        i = 0
        for drum in drums:
            pos = motor.absolute_position(drum["port"])
            if (pos >= 175 and not drumplay[i]):
                print(f"{drum['name']} playing")
                print(pos)
                await play_note(57)
                drumplay[i] = True
            elif(abs(pos) < 170):
                print("not playing")
                print(pos)
                drumplay[i] = False
            i+=1
            await runloop.sleep_ms(10)


async def play_note(note):
    Piano.on(note, velocity['f'])
    await runloop.sleep_ms(10)    
    Piano.off(note)
    
    



midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)


runloop.run(drum1(drums),readPos(drums))

print('disconnect')
midi.disconnect()
