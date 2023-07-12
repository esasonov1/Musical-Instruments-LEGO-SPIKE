
def NoteToNumber(note, octave = 4):
    notes = {"C": 60,"Db": 61,"D": 62,"Eb": 63,"E": 64,"F": 65,"Gb": 66,"G": 67,"Ab": 68, "A": 69,"Bb": 70,"B": 71}
    
    if octave > 8 or octave < 0:
        print("Enter a valid octave!")
        raise Exception("Invalid octave input")
    
    
    note_exisits = false
    
    for i in range(11):
        if(note == notes[i]):
            note_exisits = True
            print(note_exisits)
        elif(i == 11 and note_exisits == False):
            raise Exception("Invalid note input")
            print("Enter a valid note!")  
                   
             
    
    try:
           
        if (octave == 8 and note == "C"):
            notes[note] = 108   
        if ((octave > 4) and (octave < 8)):
            notes[note] = notes[note] + (octave-4)*12
        if ((octave < 4) and (octave > -1)):
            notes[note] = notes[note] + (octave-4)*12        
        return(notes[note])
    except: 
        print("Enter a valid input!")         
    
    
done = False
while not done:
    try:
        NoteToNumber("Eb", 4)
        done = True
    except Exception as e:
        if e == "Invalid octave input":
            continue
        if e == "Invalid note input":
            continue
     
            
    

