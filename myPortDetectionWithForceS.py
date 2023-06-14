import time
from ble_MIDI import *
from hub import *
import device
import force_sensor


deviceTypeLookup = {48: 'm', 49: 'M', 61: 'Color S', 62: 'Distance S', 63: 'Force S', 255: 'N'}

deviceType = [0] * 6


def ReadPorts():
    for i in range(6):
        deviceType[i] = deviceTypeLookup.get(device.device_id(i), 'N')
    return deviceType

def ConvertPortID(port_id):
    port_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    return f"port.{port_letters[port_id]}"

def CheckPort(device_type):
    for port_id in range(len(deviceType)):
        if deviceType[port_id] == device_type:
            return ConvertPortID(port_id)
    return None

def portDetection(sensor_type):
    deviceType = ReadPorts()
    port = CheckPort(sensor_type)
    if port is not None:
        print(f"{sensor_type} is connected to {port}")
        return port
    else:
        print(f"{sensor_type} is not connected")
        return None

def done(): 
    return button.pressed(button.RIGHT)
    
def velocity():
    detected_port = portDetection('Force S')
    
    velocity_range = 127
    velocity_value = int((force_sensor.force(detected_port) / 100) * velocity_range)

    return velocity_value
    
def play_note(note):
    #vel = velocity()
    #Piano.on(note, vel)
    Piano.on(note)
    time.sleep(0.1)
    Piano.off(note)
    time.sleep(0.1)

def activated():
    detected_port = portDetection('Force S')
    if detected_port is not None:
        return force_sensor.force(eval(detected_port)) > 0
    return False


midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)

while not done():
    if activated():
        print("Activated")
        time.sleep(.5)
        play_note(48)
    else:
        print("NOT Activated")
        time.sleep(.5)

print('Disconnect')
midi.disconnect()
