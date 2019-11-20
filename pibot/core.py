from pibot import motor
from pibot import ultrasound 

class this:
    state = "stop"


def init():
    motor.GPIO_motor_setup()
    ultrasound.GPIO_ultrasound_setup()
    print("Pibot has been initialized.")


def operate():

    if this.state == "stop":
        return

    print("Hello World!")


def set_state(state):

    if state not in("start", "stop"):
        return "Canno set state; invalid argument."

    else:
        this.state = state
        return "State set to: " + state


def get_dist():
    return ultrasound.measurement()

def set_dir(dir):
    motor.set_dir(dir)

def get_motors():
    return "Left motor: " + str(420) + "Right motor: " + str(6969)
