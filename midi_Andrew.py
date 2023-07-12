import struct
import ble_CBR
import bluetooth
import button
import time
import force_sensor as fs
import port,time

p1 = port.PORTA
p2 = port.PORTB
p3 = port.PORTC

NoteOn = 0x90
NoteOff = 0x80
MaxVol = 127
MinVol = 0

done = lambda : button.button_pressed(button.BUTTON_RIGHT)

package = [0x00,0x00,0x00,0x00,0x00]

def note(cmd,value,volume):
    timestamp_ms = time.ticks_ms()
    package[0] = (timestamp_ms >> 7 & 0b111111) | 0x80
    package[1] =  0x80 | (timestamp_ms & 0b1111111)
    package[2] =  0x80 | cmd
    package[3] = value
    package[4] = volume
    return struct.pack("bbbbb", package[0], package[1], package[2], package[3], package[4])

def Piano():
    ble = bluetooth.BLE()
    p = ble_CBR.BLESimplePeripheral(ble, 'MIDI', 'MySPIKE')

    def on_rx(v):
        print("RX", v)
    
    p.on_write(on_rx)
        
    was_connected = False
    
    while not done():
        if p.is_connected():
            vel = 10 * fs.get_touch(p1)
            NoteO = NoteOn if vel != 0 else NoteOff
            p.send(note(NoteOn,60,vel))
            vel = 10 * fs.get_touch(p2)
            NoteO = NoteOn if vel != 0 else NoteOff
            p.send(note(NoteOn,65,vel))
            vel = 10 * fs.get_touch(p3)
            NoteO = NoteOn if vel != 0 else NoteOff
            p.send(note(NoteOn,67,vel))
            time.sleep(0.02)
            #p.send(note(NoteOff,60,MinVol))
            #time.sleep(0.5)
            #was_connected = True
        else:
            if was_connected:
                break
        time.sleep_ms(1000)
    
Piano()
