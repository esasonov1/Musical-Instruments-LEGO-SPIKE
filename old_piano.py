import struct
import ble_CBR
import bluetooth
import button
import time

notes = [60,61,62,63,64,63,62,61]

NoteOn = 0x90
NoteOff = 0x80
Reset = 0xFF

velocity = {'off':0, 'pppp':8,'ppp':20,'pp':31,'p':42,'mp':53,
    'mf':64,'f':80,'ff':96,'fff':112,'ffff':127}

instruments = {'Acoustic Grand Piano':0,'Bright Acoustic Piano':1,'Electric Grand Piano':2,'Honky-tonk Piano':3,'Rhodes Piano':4,'Chorused Piano':5,'Harpsichord':6,'Clavinet':7,'Celesta':8,'Glockenspiel':9,'Music box':10,'Vibraphone':11,'Marimba':12,'Xylophone':13,'Tubular Bells':14,'Dulcimer':15,'Hammond Organ':16,'Percussive Organ':17,'Rock Organ':18,'Church Organ':19,
    'Reed Organ':20,'Accordion':21,'Harmonica':22,'Tango Accordion':23,'Acoustic Guitar (nylon)':24,'Acoustic Guitar (steel)':25,'Electric Guitar (jazz)':26,'Electric Guitar (clean)':27,'Electric Guitar (muted)':28,'Overdriven Guitar':29,'Distortion Guitar':30,'Guitar Harmonics':31,'Acoustic Bass':32,'Electric Bass (finger)':33,'Electric Bass (pick)':34,'Fretless Bass':35,
    'Slap Bass 1':36,'Slap Bass 2':37,'Synth Bass 1':38,'Synth Bass 2':39,'Violin':40,'Viola':41,'Cello':42,'Contrabass':43,'Tremolo Strings':44,'Pizzicato Strings':45,'Orchestral Harp':46,'Timpani':47,'String Ensemble 1':48,'String Ensemble 2':49,'Synth Strings 1':50,'Synth Strings 2':51,'Choir Aahs':52,'Voice Oohs':53,'Synth Voice':54,'Orchestra Hit':55,'Trumpet':56,
    'Trombone':57,'Tuba':58,'Muted Trumpet':59,'French Horn':60,'Brass Section':61,'Synth Brass 1':62,'Synth Brass 2':63,'Soprano Sax':64,'Alto Sax':65,'Tenor Sax':66,'Baritone Sax':67,'Oboe':68,'English Horn':69,'Bassoon':70,'Clarinet':71,'Piccolo':72,'Flute':73,'Recorder':74,'Pan Flute':75,'Bottle Blow':76,'Shakuhachi':77,'Whistle':78,'Ocarina':79,'Lead 1 (square)':80,
    'Lead 2 (sawtooth)':81,'Lead 3 (calliope lead)':82,'Lead 4 (chiffer lead)':83,'Lead 5 (charang)':84,'Lead 6 (voice)':85,'Lead 7 (fifths)':86,'Lead 8 (brass + lead)':87,'Pad 1 (new age)':88,'Pad 2 (warm)':89,'Pad 3 (polysynth)':90,'Pad 4 (choir)':91,'Pad 5 (bowed)':92,'Pad 6 (metallic)':93,'Pad 7 (halo)':94,'Pad 8 (sweep)':95,'FX 1 (rain)':96,'FX 2 (soundtrack)':97,
    'FX 3 (crystal)':98,'FX 4 (atmosphere)':99,'FX 5 (brightness)':100,'FX 6 (goblins)':101,'FX 7 (echoes)':102,'FX 8 (sci-fi)':103,'Sitar':104,'Banjo':105,'Shamisen':106,'Koto':107,'Kalimba':108,'Bagpipe':109,'Fiddle':110,'Shana':111,'Tinkle Bell':112,'Agogo':113,'Steel Drums':114,'Woodblock':115,'Taiko Drum':116,'Melodic Tom':117,'Synth Drum':118,'Reverse Cymbal':119,
    'Guitar Fret Noise':120,'Breath Noise':121,'Seashore':122,'Bird Tweet':123,'Telephone Ring':124,'Helicopter':125,'Applause':126,'Gunshot':127}


done = lambda : button.button_pressed(button.BUTTON_RIGHT)

def note(cmd, value, volume, channel = 0):
    channel = 0x0F & channel
    timestamp_ms = time.ticks_ms()
    tsM = (timestamp_ms >> 7 & 0b111111) | 0x80
    tsL =  0x80 | (timestamp_ms & 0b1111111)
    c =  cmd | channel
    d1 = value
    d2 = volume
    return struct.pack("bbbbb", tsM,tsL,c,d1,d2)

def chord(cmd, value, volume, channel = 0):
    channel = 0x0F & channel
    timestamp_ms = time.ticks_ms()
    tsM = (timestamp_ms >> 7 & 0b111111) | 0x80
    tsL =  0x80 | (timestamp_ms & 0b1111111)
    c =  cmd | channel
    d1 = value
    d2 = volume
    return struct.pack("bbbbb", tsM,tsL,c,d1,d2)
    
def instrument(value = 57, channel = 0):
    timestamp_ms = time.ticks_ms()
    tsM = (timestamp_ms >> 7 & 0b111111) | 0x80
    tsL =  0x80 | (timestamp_ms & 0b1111111)
    c =  0x80 | (0b11000000 + 0x0F & channel)
    d1 = value
    return struct.pack("bbbb", tsM, tsL, c, d1)
    
def Piano():
    ble = bluetooth.BLE()
    p = ble_CBR.BLESimplePeripheral(ble, 'MIDI', 'chris')

    def on_rx(v):
        print("RX", v)
    
    p.on_write(on_rx)
        
    was_connected = False
    if p.is_connected():
        p.send(Reset)
    
    while not done():
        if p.is_connected():
            p.send(instrument(instruments['Acoustic Grand Piano'],0))
            p.send(instrument(instruments['Trumpet'],1))
            for x in notes:
                p.send(note(NoteOn,x,velocity['ffff'],0))
                p.send(note(NoteOn,x,velocity['ffff'],1))
                time.sleep(0.5)
                p.send(note(NoteOff,x,velocity['off'],0))
                p.send(note(NoteOff,x,velocity['off'],1))
                time.sleep(0.5)
                
            #was_connected = True
        else:
            if was_connected:
                break
        time.sleep_ms(1000)


Piano()
