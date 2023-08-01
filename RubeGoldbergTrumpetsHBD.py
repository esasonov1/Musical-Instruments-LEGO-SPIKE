from ble_emma import *
from ble_MIDI import *
from hub import light_matrix
import runloop
from hub import port
import force_sensor
import time
from app import music
import color_sensor
import color
import motor


def hbd():
    while True:
        if color_sensor.reflection(port.C) is color.RED:
            #Right now the blue color detection is picking up everything, not just blue
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(475)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,175)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(400)
            #note2 d
            #motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.E,-130,175)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.E,-90,100)
            time.sleep_ms(500)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,125)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(500)
            #note3 f
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.D,-130,125)
            time.sleep_ms(550)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(500)
            #note4 e
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.F,-60,200)
            time.sleep_ms(350)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(1000)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(475)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,125)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(500)
            #note2 d
            #motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.E,-130,175)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.E,-90,100)
            time.sleep_ms(500)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,150)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(700)
            #note5 g
            motor.run_to_absolute_position(port.B,160,120)
            time.sleep_ms(150)
            #^changed speed from 100
            motor.run_to_absolute_position(port.D,-130,90)
            time.sleep_ms(750)
            motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(800)
            #note3 f
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.D,-130,125)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(1000)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(400)
            #note1 c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.B,150,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            time.sleep_ms(500)
            #note1 high c
            #motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.E,-130,140)
            motor.run_to_absolute_position(port.D,-130,100)
            time.sleep_ms(750)
            motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(800)
            #note7 a
            #motor.run_to_absolute_position(port.B,90,100)
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.B,150,140)
            time.sleep_ms(150)
            motor.run_to_absolute_position(port.F,-60,100)
            time.sleep_ms(750)
            motor.run_to_absolute_position(port.B,90,120)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(400)
            #note3 f
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.D,-130,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(400)
            #note4 e
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.F,-60,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(300)
            #note2 d
            #motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.E,-130,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.E,-90,100)
            time.sleep_ms(1000)
            #note6 b
            #motor.run_to_absolute_position(port.E,-90,100)
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.E,-130,120)
            time.sleep_ms(150)
            motor.run_to_absolute_position(port.F,-60,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(400)
            #note6 b
            #motor.run_to_absolute_position(port.E,-90,100)
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.E,-130,120)
            time.sleep_ms(150)
            motor.run_to_absolute_position(port.F,-60,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.E,-90,100)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(500)
            #note7 a
            #motor.run_to_absolute_position(port.B,90,100)
            #motor.run_to_absolute_position(port.F,-90,100)
            motor.run_to_absolute_position(port.B,150,140)
            time.sleep_ms(150)
            motor.run_to_absolute_position(port.F,-60,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.F,-90,100)
            time.sleep_ms(500)
            #note3 f
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.D,-130,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(400)
            #note5 g
            #motor.run_to_absolute_position(port.B,90,100)
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.B,160,120)
            time.sleep_ms(150)
            motor.run_to_absolute_position(port.D,-130,90)
            time.sleep_ms(600)
            motor.run_to_absolute_position(port.B,90,100)
            motor.run_to_absolute_position(port.D,-90,100)
            time.sleep_ms(500)
            #note3 f
            #motor.run_to_absolute_position(port.D,-90,100)
            motor.run_to_absolute_position(port.D,-130,100)
            time.sleep_ms(500)
            motor.run_to_absolute_position(port.D,-90,100)
def main():
    while True:
        hbd()
main()



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
#disconnect()





























'''
while not done():
    if Force_Sensor_Activated(port.C) and Force_Sensor_Activated(port.B):
        play_note("Force S",NoteToNumber("E",3), .5, "ffff", port.C)
    
    elif Force_Sensor_Activated(port.B) and Force_Sensor_Activated(port.A):
        play_note("Force S",NoteToNumber("G",3), .5, "ffff", port.B)
    
    elif Force_Sensor_Activated(port.A) and Force_Sensor_Activated(port.C):
        play_note("Force S",NoteToNumber("C",4), .5, "ffff", port.A)    
    
    elif Force_Sensor_Activated(port.A):
        play_note("Force S",NoteToNumber("C",3), .5, "ffff", port.A)
    
    elif Force_Sensor_Activated(port.B):
        play_note("Force S",NoteToNumber("D",3), .5, "ffff", port.B)
    
    elif Force_Sensor_Activated(port.C):
        play_note("Force S",NoteToNumber("F",3), .5, "ffff", port.C)
    
    else:
        time.sleep(.5)
'''   
