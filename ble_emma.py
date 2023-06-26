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
hubPorts = {'A': 'N', 'B': 'N', 'C': 'N', 'D': 'N', 'E': 'N', 'F': 'N'}

drumNotes ={'Closed Hi-Hat': 31, 'Rim Shot': 32, 'Pedal Hi-Hat': 33,'Snare Drum': 34,
    'Side Stick': 37,'Hand Clap': 39,'Low Tom': 41,'Closed Hi-Hat': 42,'Low Tom': 43,
    'Pedal Hi-Hat': 44,'Mid Tom': 45,'Open Hi-Hat': 46,'Mid Tom': 47,'High Tom': 48,
    'Crash Cymbal': 49,'High Tom': 50,'Ride Cymbal': 51,'Ride Cymbal': 52,'Ride Bell': 53,
    'Shaker': 54,'Crash Cymbal': 57,'Ride Cymbal': 59,'Snare Drum': 86,'Closed Hi-Hat': 90,
    'Low Tom': 91,'Closed Hi-Hat': 92,'Pedal Hi-Hat': 94,'Mid Tom': 95,'High Tom': 96,
    'Ride Cymbal': 99}


#initialize

#firmware_check()
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)


def done():
    return button.pressed(button.RIGHT)


def test():
    print("hi Emma!")


def play_note(sensor, note, duration, dynamics = 'ff'):
    
    #print("in play_note")
        
    if (sensor == "Force S"):
        if Force_Sensor_Activated():
            play_the_note(note, duration, dynamics)
        else:
            print("waiing for FS activation")
            time.sleep(.1)
            
    elif (sensor == "Color S"):
        if Color_Sensor_Activated():
            play_the_note(note, duration, dynamics)
        else:
            print("waiting for CS activation")
            time.sleep(.1)
            
    elif (sensor == "Distance S"):
        if Distance_Sensor_Activated():
            the_port = check_port_connection("Distance S")
            dist = distance_sensor.distance(the_port)
            dist_note = get_note_from_distance(dist)
            play_the_note(dist_note, duration, dynamics)
            #play_the_note(note, duration)
        else:
            print("waiting for DS activation")
            time.sleep(.1)
            
    elif ((sensor == "m") or (sensor == "M")):
        #Need and if activated statment bc it could be not conencted
        the_port = check_port_connection(sensor)
        mpos = motor.absolute_position(the_port)
    
        if mpos < 0:
            mpos = mpos + 360  
        
        print(mpos)
        
        note_range = 108 - 21  #Total number of notes in the range
        note_value = int((mpos / 360) * note_range) + 21  #Maps the notes and value

        play_the_note(note_value, .1, dynamics)
        
    else: 
        print("ELSE!!")
        time.sleep(2)       


def play_chord(a, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    Piano.on([a,b,c,d,e,f,g,h],velocity['f'])
    time.sleep(.5)
    Piano.off([a,b,c,d,e,f,g,h])
        
        
def play_the_note(note, duration, dynamics):
    Piano.on(note, velocity[dynamics])
    time.sleep(duration)
    Piano.off(note)


def Force_Sensor_Activated():
    try:
        the_port = check_port_connection("Force S")
        if the_port is None:
            #print("Please connect the Force Sensor!")
            raise Exception("Force Sensor is NOT connected")

        if force_sensor.force(the_port) > 0:
            print("Force Sensor is ACTIVATED")
            return True
        else:
            #print("FS FALSE")
            #time.sleep(.25)
            return False
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False
    
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
    
        
def Distance_Sensor_Activated():
    try:
        the_port = check_port_connection("Distance S")
        if the_port is None:
            #print("Please connect the Distance Sensor!")
            raise Exception("Distance Sensor is NOT connected")
        
        if distance_sensor.distance(the_port) > 0:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False    


#def Motor_Activated():
    

def disconnect():
    print('disconnect')
    midi.disconnect()




def NoteToNumber(note, octave = 0):
    notes = {"C": 24,"Db": 25,"D": 26,"Eb": 27,"E": 28,"F": 29,"Gb": 30,"G": 31,"Ab": 32, "A": 33,"Bb": 34,"B": 35}
    
    try:  
        if octave > 8 or octave < 0:
            raise Exception("Invalid octave input")
        if note not in notes:
            raise Exception("Invalid note input")
    
        if(octave > 0):
            return((notes[note]) + (octave*12))
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False
        
    
'''-----Helper functions section (NOT intended for the user to use!)-----'''

def firmware_check():
    try:
        version.atlantis
        print(version.atlantis)
        print("Firmware is up to date! Good Job!")
    except:
        print("Old Firmware: Please update your LEGO SPIKE hub to the latest firmware!")


def get_note_from_distance(dist):
    if dist == -1 or dist > 500:
        return -1
    elif dist < 500:
        note = int(8 + (dist / 5))
        return note



def ReadPorts():   
    i = 0
    for key in sorted(hubPorts): 
        hubPorts[key] = deviceTypeLookup.get(device.device_id(i))
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

    i = 0
    for port in sorted(hubPorts):
        
        if hubPorts[port] == sensor:
            #print("connected")
            return string2port(f"port.{port}")
            #return(f"port.{port}")
    
        if i == 5:
            print(f"{sensor} is NOT connected")
            print("--------------")
            #raise Exception(f"{sensor} is NOT connected")
            return None
    i+=1

    return None
        
    
def string2port(portS):
    if portS == "port.A": return port.A
    if portS == "port.B": return port.B
    if portS == "port.C": return port.C
    if portS == "port.D": return port.D
    if portS == "port.E": return port.E
    if portS == "port.F": return port.F
