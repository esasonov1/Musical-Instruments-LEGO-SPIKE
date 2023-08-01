from ble_emmaREDO import *
import motor
import force_sensor
import motor
import hub


while not done():    
    
    if Force_Sensor_Activated(port.B):
        play_note("Force S", "Snare Drum", .2, "ffff", port.B)
        
    if Force_Sensor_Activated(port.A):
        play_note("Force S", "Low Tom", .2, "ffff", port.A)
        
    if Force_Sensor_Activated(port.C):
        play_note("Force S", "Ride Cymbal", .2, "ffff", port.C)
        
    if Force_Sensor_Activated(port.D):
        play_note("Force S", "Crash Cymbal", .2, "ffff", port.D)
        
    if Color_Sensor_Activated(port.F):
        play_note("Color S", "High Tom", .2, "ffff", port.F)
        
    if Color_Sensor_Activated(port.E):
        play_note("Color S", "Mid Tom", .2, "ffff", port.E)
   
   

