from ble_emmaREDO import *
import motor
import force_sensor
import motor
import hub


while not done():    
    
    if Force_Sensor_Activated(port.B):
        play_note("m", 60, .2, "ffff", port.A)
   