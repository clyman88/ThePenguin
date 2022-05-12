# Luke Frank & Cole Lyman
# Engineering 4 Pi in the Sky - Mr. Miller
# 5/12/22

# Making a test file to try use the button feature

# Import servo libraries
from gpiozero import Servo
from time import sleep

# Import GPIO library for push button
import RPi.GPIO as GPIO 

# Specify push-button parameters:

def button_callback(channel):
    print("Button was pushed!") # Test code to make sure button works
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


# Set servo to pin number
servo = Servo(25)

# Code starts out with the servo arms fully extended.
# Min = extended. Max = retracted.
servo.min()

while True:
  if GPIO.input(10) == GPIO.HIGH:
          print("Button was pushed!")
          time.sleep(1)
        
          print("Servo retracts in five")
          time.sleep(5)
          
          print("Servo retracting...")
          servo.max()
          
          time.sleep(3)
          print("Back to extended")
          servo.min()
          
          # break
          # Should go back to activating at button press
                
# For when the MPU 6050 is added...
# sudo pip3 install adafruit-circuitpython-mpu6050
# Link for sources:
# https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro/python-and-circuitpython
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

#import adafruit_mpu6050

#i2c = board.I2C()
#mpu = adafruit_mpu6050.MPU6050(i2c)
# while True:
    #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    #print("Temperature: %.2f C" % mpu.temperature)
    #print("")
    #time.sleep(1)
