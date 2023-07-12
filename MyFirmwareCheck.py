#from ble_emma import *
from ble_MIDI import *
from hub import *
import version


def firmware_check():
    try:
        version.atlantis
        print(version.atlantis)
        print("Firmware is up to date! Good Job!")
    except:
        print("Old Firmware: Please update your LEGO SPIKE hub to the latest firmware!")



firmware_check()


