import board
import pwmio
import time

led = pwmio.PWMOut(board.GP14, variable_frequency=True)
led.frequency = 500 # hz

while True:
    # 0 to 65535 in steps of 100, 
    # for 0% to 100% duty cycle
    for i in range(0, 65535, 100):
        led.duty_cycle = i
        time.sleep(0.01)