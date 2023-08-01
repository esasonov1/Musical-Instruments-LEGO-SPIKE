import time
import ble_CBR
import bluetooth
import ble_advertising
from ble_MIDI import *
from hub import *
import device
import force_sensor
import distance_sensor
import motor
import color_sensor
import struct
import version


#global
deviceTypeLookup = {48: 'm', 49: 'M', 61: 'Color S', 62: 'Distance S', 63: 'Force S', 255: 'N'}
hubPorts = {'A': ['N', False], 'B': ['N',False], 'C': ['N',False], 'D': ['N',False], 'E': ['N',False], 'F': ['N',False]}


def play_note(sensor, note, duration, dynamics = 'ff'):
    if (sensor == "Color S"):
        if Color_Sensor_Activated():
            play_the_note(note, duration, dynamics)
        else:
            print("waiting for CS activation")
            time.sleep(.1)
        
    else: 
        print("ELSE!!")
        time.sleep(2)       


def Color_Sensor_Activated():
    try:
        the_port = check_port_connection("Color S")

        if the_port is None:
            #print("Please connect the Color Sensor!")
            raise Exception("Color Sensor is NOT connected")

        reflection = color_sensor.reflection(the_port)
        if reflection > 50:
            print("Color Sensor is ACTIVATED")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False
    


def ReadPorts():   
    i = 0
    for key in sorted(hubPorts): 
        #print(deviceTypeLookup.get(device.device_id(i)))
        hubPorts[key][0] = deviceTypeLookup.get(device.device_id(i))
        i+=1
            
    return None


def is_connected(sensor):
    ReadPorts()
    
    there_is_sensor = False
    
    i = 0
    for port in sorted(hubPorts):
        
        if hubPorts[port] == sensor:
            print(f"{sensor} is connected to port.{port}")
            there_is_sensor = True
    
        if i == 5 and not there_is_sensor:
            print(f"{sensor} is NOT connected")
            print("--------------")
            raise ValueError(f"{sensor} is not connected to any port")
            return False
            
        if i == 5 and there_is_sensor:
            return True
            
        i+=1

    return False


def check_port_connection(sensor):
    ReadPorts()
    print("Checking port conenction")
    i = 0
    for port in sorted(hubPorts):
        print("loop?")
        
        if hubPorts[port][0] == sensor:
            print("connected")
            if hubPorts[port][1] == False:
                print(f"Nice! Its in port.{port}")
                hubPorts[port][1] = True  
                hubPorts[port]
                return string2port(f"port.{port}")
                #return(f"port.{port}")   
            else:
                print("somethings already here, try again")
                continue

    
        if i == 5:
            print(f"{sensor} is NOT connected")
            print("--------------")
            #raise Exception(f"{sensor} is NOT connected")
            return None
        i+=1
        
    print("returnnnn")
    return None
  
   
    
def string2port(portS):
    if portS == "port.A": return port.A
    if portS == "port.B": return port.B
    if portS == "port.C": return port.C
    if portS == "port.D": return port.D
    if portS == "port.E": return port.E
    if portS == "port.F": return port.F


'''
ReadPorts()
print(hubPorts)
print(hubPorts['B'][1])
print(hubPorts['B'][0])
print(sorted(hubPorts))

#play_note("Color S", 50, 1)
#check_port_connection("Color S")
#check_port_connection("Color S")
#check_port_connection("Color S")
#check_port_connection("Color S")
'''
