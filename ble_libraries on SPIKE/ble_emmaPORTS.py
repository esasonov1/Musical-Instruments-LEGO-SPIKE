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
#import version


#global
deviceTypeLookup = {48: 'm', 49: 'M', 61: 'Color S', 62: 'Distance S', 63: 'Force S', 255: 'N'}
hubPorts = {'A': 'N', 'B': 'N', 'C': 'N', 'D': 'N', 'E': 'N', 'F': 'N'}

drumNotes = {31: 'Closed Hi-Hat', 32: 'Rim Shot', 33: 'Pedal Hi-Hat', 34: 'Snare Drum',
    37: 'Side Stick', 39: 'Hand Clap', 41: 'Low Tom', 42: 'Closed Hi-Hat', 43: 'Low Tom',
    44: 'Pedal Hi-Hat', 45: 'Mid Tom', 46: 'Open Hi-Hat', 47: 'Mid Tom', 48: 'High Tom',
    49: 'Crash Cymbal', 50: 'High Tom', 51: 'Ride Cymbal', 52: 'Ride Cymbal', 53: 'Ride Bell',
    54: 'Shaker', 57: 'Crash Cymbal', 59: 'Ride Cymbal', 86: 'Snare Drum', 90: 'Closed Hi-Hat',
    91: 'Low Tom', 92: 'Closed Hi-Hat', 94: 'Pedal Hi-Hat', 95: 'Mid Tom',96: 'High Tom',
    99: 'Ride Cymbal'}


#firmware_check()

def done():
    return button.pressed(button.RIGHT)


def test():
    print("hi Emma!")


def play_note(sensor = "N", note = 60, duration = 1, dynamics = 'fff', port = None):
    
    #print("in play_note")

    if type(note) == str:  
        for key, value in drumNotes.items():
            if value == note:
                note = key  
                #print("Found note:", note)

            
    if (sensor == "N"):  
        play_the_note(note, duration, dynamics)    
        
    elif (sensor == "Force S"):
        if Force_Sensor_Activated(port):
            play_the_note(note, duration, dynamics)
        else:
            print("waiing for FS activation")
            time.sleep(.1)
            
    elif (sensor == "Color S"):
        if Color_Sensor_Activated(port):
            play_the_note(note, duration, dynamics)
        else:
            print("waiting for CS activation")
            time.sleep(.1)
            
    elif (sensor == "Distance S"):
        if Distance_Sensor_Activated(port):
            the_ports = check_port_connection("Distance S")
            for port in the_ports:
                if distance_sensor.distance(port) > 0:
                    dist = distance_sensor.distance(port)
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
        print("ELSE!!Invalid sensor type")
        time.sleep(.5)       


def play_chord(a, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    Piano.on([a,b,c,d,e,f,g,h],velocity['ff'])
    time.sleep(.5)
    Piano.off([a,b,c,d,e,f,g,h])
        
        
def play_the_note(note, duration, dynamics):
    Piano.on(note, velocity[dynamics])
    time.sleep(duration)
    Piano.off(note, velocity[dynamics])


def Force_Sensor_Activated(port):
    try:
        if port is None:
            the_ports = check_port_connection("Force S")
            if the_ports is None:
                #print("Please connect the Force Sensor!")
                raise Exception("Force Sensor is NOT connected")
            
            for port in the_ports:
                if force_sensor.force(port) > 0:
                    print("Force Sensor is ACTIVATED")
                    return True
            
            return False
        else:
            #print("Port was typed") 
            if force_sensor.force(port) > 0:
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


    
def Color_Sensor_Activated(port):
    try:
        if port is None:
            the_ports = check_port_connection("Color S")
            if the_ports is None:
                #print("Please connect the Color Sensor!")
                raise Exception("Color Sensor is NOT connected")
            
            for port in the_ports:
                if color_sensor.reflection(port) > 50:
                    print("Color Sensor is ACTIVATED")
                    return True
            
            return False
        else:
            if color_sensor.reflection(port) > 50:
                print("Color Sensor is ACTIVATED")
                return True
            else:
                return False
                
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)
        return False

        
def Distance_Sensor_Activated(port):
    try:
        if port is None:
            the_ports = check_port_connection("Distance S")
            if the_ports is None:
                #print("Please connect the Color Sensor!")
                raise Exception("Distance Sensor is NOT connected")
            
            for port in the_ports:
                if distance_sensor.distance(port) > 0:
                    print("Distance Sensor is ACTIVATED")
                    return True

            return False
        else:
            if distance_sensor.distance(port) > 0:
                print("Distance Sensor is ACTIVATED")
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
    listOfPorts = []
    is_a_connection = False
    i = 0
    for port in sorted(hubPorts):
        
        if hubPorts[port] == sensor:      
            listOfPorts.append(string2port(f"port.{port}"))
            is_a_connection = True
            #return string2port(f"port.{port}")
            #return(f"port.{port}")
    
        if i == 5 and is_a_connection:
            #print(listOfPorts)
            return listOfPorts
            
            
        if i == 5 and not is_a_connection:
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



#initialize
midi = MIDI_Player('emma')
midi.wait_for_connection()
Piano = MIDI_Instrument(midi, instruments['Acoustic Grand Piano'], channel=0)
