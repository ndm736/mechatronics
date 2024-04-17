import time # for time.sleep()
import board # for pin names
import analogio # for adc

a0 = analogio.AnalogIn(board.A0) # read the voltage on A0
a1 = analogio.AnalogIn(board.A1) # read the voltage on A1

while 1:
    print("("+str(a0.value)+","+str(a1.value)+")")
    time.sleep(1/30) # print out 30 times per second
