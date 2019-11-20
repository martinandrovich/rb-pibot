import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

DutyCycleA = 50
DutyCycleB = 50

Stop = 0

pwmMotorAForwards = None
pwmMotorABackwards = None
pwmMotorBForwards = None
pwmMotorBBackwards = None

# GPIO setup
def GPIO_motor_setup():

    global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Motor frequency
    Frequency = 100
    Stop = 0
    
    GPIO.setup(pinMotorAForwards, GPIO.OUT)
    GPIO.setup(pinMotorABackwards, GPIO.OUT)
    GPIO.setup(pinMotorBForwards, GPIO.OUT)
    GPIO.setup(pinMotorBBackwards, GPIO.OUT)
    
    # Set the GPIO to software PWM at 'Frequency' Hertz
    pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
    pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
    pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
    pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
    
    # Start the software PWM with a duty cycle of 0 (i.e. not moving)
    pwmMotorAForwards.start(Stop)
    pwmMotorABackwards.start(Stop)
    pwmMotorBForwards.start(Stop)
    pwmMotorBBackwards.start(Stop)
    return

# Turn all motors off
def stopmotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def forward(A, B):
    pwmMotorAForwards.ChangeDutyCycle(A)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(B)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def backward():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def left():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

                                                                                
# Turn Right
def right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

def set_dir(direction):
    if direction == "left":
        forward(40,50)
    elif direction == "right":
        forward(50,40)
    else:
        forward(50,50)

# Clean Up
def clean_up_motor():
    GPIO.cleanup()

GPIO_motor_setup()

set_dir("right")

time.sleep(5)

set_dir("left")

time.sleep(5)

set_dir("forward")

time.sleep(5)

stopmotors()

clean_up_motor()
