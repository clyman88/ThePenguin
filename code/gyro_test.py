# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_mpu6050
import csv

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['x_accel', 'y_accel', 'z_accel']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'x_accel': 'x_accel:%.2f', 'y_accel': 'y_accel:%.2f', 'z_accel': 'z_accel:%.2f'})
        time.sleep(1)


   # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
   # print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
   # print("Temperature: %.2f C" % mpu.temperature)
   # print("")
   # time.sleep(1)
