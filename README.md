# MUSICAL INSTRUMNETS LEGO SPIKE
Emma Sasonov, 8/1/2023


Purpose: A library to be used on the LEGO SPIKE Prime that allows kids to build instruments
         with LEGO SPIKE sensors that can play notes through MIDI on GarageBand using an iPad/iPhone.
         This library contains simple and easy to use functions that can be called to create fun
         and cool instruments!


*Note: There are several variations of ble_emma... this is because some include automatic port detection
      while others only work for previous SPIKE firmwares. Some of the latest updates dont work
      on a few of the librarys.

              
Instructions:
1. Load ble_advertising.py, ble_CBR.py, and ble_emma to your SPIKE Prime
2. Either use example code to create a music or use functions from my library by importing ble_emma
3. Run code (When you run your code, it should say “Waiting.....") 
4. Open up Garage Band
5. Select an Instrument (any instrument!)
      - Press the settings button on the top right of your screen (⚙)
      - Click Advanced 
      - Click Bluetooth MIDI Devices
      - Select the name that appears (should first say Not Connected and then change to Connected)
             - Feel free to change the name of the connection in your code!(8 char max)            
6. Plays some cool music! 🎶 (make sure to use some LEGO SPIKE sensors in your build!)

Once up and running, try recording your music in GarageBand!

Good luck! :)
