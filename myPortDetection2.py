import time
from ble_MIDI import *
from hub import *
import device


deviceTypeLookup = {48:'m', 49:'M', 61:'Color S', 62:'Distance S', 63:'Force S', 255:'N'}
deviceType = [0] * 6


#Sets each value in deviceType array equal to what is currently plugged
#into the port by looking up the device id at the port in the dictionary
#and then returns the new array
def ReadPorts():
    for i in range(6):
        deviceType[i] = deviceTypeLookup.get(device.device_id(i))
        #print(deviceType[i])
    return deviceType





def ConvertPortID(port_number):
    port_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    return f"port.{port_letters[port_number]}"



#takes in a name of a sensor, checks where in 
def CheckPort(item):
    
    for port_number in range(6):
        
        if deviceType[port_number] == item:
            return ConvertPortID(port_number)
            
    return None


def check_port_connections():
    device_type = ReadPorts()
    print(device_type)
    
    for item in device_type:
        port = CheckPort(item)
        if item == 'N':
            print(f"Nothing is connected to {port}")
        else:
            print(f"{item} is connected to {port}")
        
        
            
    print("--------------")
    time.sleep(1)  
                    
    
                

check_port_connections()
