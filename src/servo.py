import board
import pwmio
import time

servo = pwmio.PWMOut(board.GP16, variable_frequency=True)
servo.frequency = 50 # hz

while True:
    # pulse 0.5 ms to 2.5 ms out of a possible 20 ms
    # for 0 degrees to 180 degrees
    # so duty_cycle can be 65535*0.5/20 to 65535*2.5/20
    
    for i in range(int(65535*0.5/20), int(65535*2.5/20), 100):
        servo.duty_cycle = i
        time.sleep(0.1)