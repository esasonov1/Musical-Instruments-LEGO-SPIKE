from hub import light_matrix
from hub import port
from hub import *
from ble_emmaPORTS import *

import color
import runloop
import force_sensor
import time
import motor



while True:

    print(force_sensor.force(port.A))

    if force_sensor.is_pressed(port.A):
        brightness = int(force_sensor.force(port.A))
        distance = int(force_sensor.force(port.A) / 20)

        for i in range(distance):
            light_matrix.set_pixel(i, 0, brightness)
            light_matrix.set_pixel((-i + 4), 4, brightness)
            time.sleep(0.1)

        motor.run(port.F,(brightness*10))
    else:
        light_matrix.clear()
        motor.stop(port.F)
        time.sleep(0.1)
        
