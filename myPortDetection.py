import time
from ble_MIDI import *
from hub import *
import device


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


while True:
    deviceType = ReadPorts()

    sensor_type = 'm'
    port = CheckPort(sensor_type)
    if port is not None:
        print(f"{sensor_type} is connected to {port}")
    else:
        print(f"{sensor_type} is not connected")

    time.sleep(1)
