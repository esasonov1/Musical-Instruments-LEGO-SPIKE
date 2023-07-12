import time
from ble_MIDI import *
from hub import *
import device


deviceTypeLookup = {48: 'm', 49: 'M', 61: 'Color S', 62: 'Distance S', 63: 'Force S', 255: 'N'}
hubPorts = {'A': 'N', 'B': 'N', 'C': 'N', 'D': 'N', 'E': 'N', 'F': 'N'}


def ReadPorts():
    
    i = 0
    for key in sorted(hubPorts): 
        hubPorts[key] = deviceTypeLookup.get(device.device_id(i))
        i+=1
        
          
    return None

   

def check_port_connections():
    while True:
        ReadPorts()
        
        
        for port in sorted(hubPorts):
            if hubPorts[port] == 'N':
                print(f"Nothing is connected to port.{port}")
            else:
                print(f"{hubPorts[port]} is connected to port.{port}")

        print("--------------")
        time.sleep(5)
        

check_port_connections()
