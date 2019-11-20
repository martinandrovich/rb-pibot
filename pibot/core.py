from pibot import motor
from pibot import ultrasound 

class this:
    """Global variables."""
    state = "stop"


def init():
    motor.GPIO_motor_setup()
    ultrasound.GPIO_ultrasound_setup()
    print("Pibot has been initialized.")


def operate():

    if this.state == "stop":
        return

    ctrl_threshold()


def ctrl_simple():

    dist = get_dist()
    dir = "right"

    if dist > 10:
        dir = "right"

    else:
        dir = "left"

    # call daniel's methods

    msg = f"Distance: {dist} cm | Direction: {dir}"
    print(msg)

def ctrl_threshold():

    dist = get_dist()
    dir = "forward"

    DIST_TH = 10
    DIST_TO_WALL = 20

    if dist > DIST_TO_WALL + DIST_TH:
        dir = "right"

    elif dist < DIST_TO_WALL - DIST_TH:
        dir = "left"

    else:
        dir = "forward"

    # call daniel's methods

    msg = f"Distance: {dist} cm | Direction: {dir}"
    print(msg)


def set_state(state):

    if state not in("start", "stop"):
        return "Cannot set state; invalid argument."

    else:
        this.state = state
        return "State set to: " + state


def get_dist():
    return ultrasound.measurement()

def set_dir(dir):
    motor.set_dir(dir)

def get_motors():
    return "Left motor: " + str(420) + "Right motor: " + str(6969)
