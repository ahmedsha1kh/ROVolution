from machine import Pin, I2C, PWM
import time

# Initialize I2C on GPIO pins (SDA=Pin 0, SCL=Pin 1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Define the I2C address of the Pico
PICO_ADDRESS = 0000  # Change this to your Pico's I2C address

# Define individual motor pins on pico (change according to electrical diagram)
vMotor1 = 1
vMotor2 = 2
vMotor3 = 3
vMotor4 = 4

hMotor1 = 5
hMotor2 = 6
hMotor3 = 7
hMotor4 = 8

#create PWM objects
vMotor1_pwm = PWM(Pin(vMotor1))
vMotor2_pwm = PWM(Pin(vMotor2))
vMotor3_pwm = PWM(Pin(vMotor3))
vMotor4_pwm = PWM(Pin(vMotor4))
hMotor1_pwm = PWM(Pin(hMotor1))
hMotor2_pwm = PWM(Pin(hMotor2))
hMotor3_pwm = PWM(Pin(hMotor3))
hMotor4_pwm = PWM(Pin(hMotor4))

motors = [vMotor1_pwm, vMotor2_pwm, vMotor3_pwm, vMotor4_pwm, hMotor1_pwm, hMotor2_pwm, hMotor3_pwm, hMotor4_pwm]

def initialize_motors():
    for motor in motors:
        motor.duty_ns(1500)
    time.sleep(1)
  
