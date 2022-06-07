# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_mpu6050
import csv

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    while True:
        writer.writerow(mpu.acceleration)
        print("Acceleration (m/s^2): x:%.2f y:%.2f z:%.2f " % (mpu.acceleration) + \
              "Gyro (degrees/s): x:%.2f y:%.2f z:%.2f " % (mpu.gyro) + \
              "Temp (deg C): %.2f" % mpu.temperature)
        time.sleep(1)


   # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
   # print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
   # print("Temperature: %.2f C" % mpu.temperature)
   # print("")
   # time.sleep(1)
