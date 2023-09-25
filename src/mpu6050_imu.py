# read acceleration and angular velocity from the MPU6050 IMU
import time
import board
import busio
#import adafruit_register
import adafruit_mpu6050 # required the adafruit_register library folder to be in CIRCUITPY/lib/

i2c = busio.I2C(board.GP11, board.GP10) # the I2C pins used, (SCL, SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.accelerometer_range = adafruit_mpu6050.Range.RANGE_2_G # acceleration values from -2G to +2G
mpu.gyro_range = adafruit_mpu6050.GyroRange.RANGE_250_DPS # angular velocity values from -250dps to +250dps

while True:
    print("(%.2f, %.2f, %.2f " % (mpu.acceleration), end=", ")
    print("%.2f, %.2f, %.2f)" % (mpu.gyro))
    time.sleep(0.010)
