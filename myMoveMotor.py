import motor, port

(p1,p2) = (port.PORTA, port.PORTB)

position = port.port_getSensor(p2)[1]
speed = port.port_getSensor(p2)[0]
angle = port.port_getSensor(p2)[2]

motor.motor_move_by_degrees(p1, -360, 1000)
motor.motor_move_by_degrees(p2, 360, 2000)




power = 1000
speed = 1000
motor.motor_move_at_power(p1, power)
motor.motor_move_at_speed(p1, speed)
duration = 5000
motor.motor_move_for_time(p1, duration, speed,motor.MOTOR_END_STATE_BRAKE)
degrees = 360
motor.motor_move_by_degrees(p1, speed, degrees, motor.MOTOR_END_STATE_HOLD)
motor.motor_move_to_position(p1, speed, degrees,motor.MOTOR_END_STATE_SMART_COAST)
motor.motor_move_to_absolute_position(p1, speed, degrees,
            motor.MOTOR_MOVE_DIRECTION_CCW,
            motor.MOTOR_END_STATE_HOLD)



motor.motor_stop(p1)

motor.motor_move_for_time((p1, p2), speed, duration)
motor.motor_move_for_time((p1, p2), (1000, 4000),
        (5000, 2000),motor.MOTOR_END_STATE_FLOAT)
        
        
        
        
        

