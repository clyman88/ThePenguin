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
    writer.writerow(["x_accel", "y_accel", "z_accel", "x_gryo", "y_gryo", "z_gryo"])  # write header row
    while True:
        writer.writerow(mpu.acceleration + mpu.gyro)  # combine 3-element tuples into single 6-elements
        print("Acceleration (m/s^2): x:%.2f y:%.2f z:%.2f " % (mpu.acceleration) + \
              "Gyro (degrees/s): x:%.2f y:%.2f z:%.2f " % (mpu.gyro))
        time.sleep(1)

