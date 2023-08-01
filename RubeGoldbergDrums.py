from ble_emmaREDO import *
import motor
import force_sensor
import motor
import hub


motor.run_to_absolute_position(port.D,175,100)


while not done():    
    
    if Force_Sensor_Activated(port.B):
        play_note("Force S", "High Tom", .4, "ffff", port.B)
        
    elif Force_Sensor_Activated(port.E):
        play_note("Force S", "Rim Shot", .4, "ffff", port.E)
        motor.run_to_absolute_position(port.D,-170,100)
    elif Force_Sensor_Activated(port.C):
        play_note("Force S", "Crash Cymbal", .001, "ffff", port.C)
        motor.run_to_absolute_position(port.A,90,1000)  
        
        time.sleep(2)   
        motor.run_to_absolute_position(port.D,170,100)
        
        motor.run_to_absolute_position(port.A,180,100)
        
        
        

        ##motor.run_for_degrees(hub.port.A,90,1000)


'''

time.sleep(2)

#Happy Birthday LEGO
play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")
play_the_note(NoteToNumber("C",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("E",3), .5, "ffff")

play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")
play_the_note(NoteToNumber("C",3), .25, "ffff")
play_the_note(NoteToNumber("G",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .5, "ffff")

play_the_note(NoteToNumber("C",3), .1875, "ffff")
play_the_note(NoteToNumber("C",3), .0625, "ffff")
play_the_note(NoteToNumber("C",4), .25, "ffff")
play_the_note(NoteToNumber("A",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("E",3), .25, "ffff")
play_the_note(NoteToNumber("D",3), .25, "ffff")

play_the_note(NoteToNumber("Bb",3), .1875, "ffff")
play_the_note(NoteToNumber("Bb",3), .0625, "ffff")

play_the_note(NoteToNumber("A",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .25, "ffff")
play_the_note(NoteToNumber("G",3), .25, "ffff")
play_the_note(NoteToNumber("F",3), .5, "ffff")
   
'''        
        
       
