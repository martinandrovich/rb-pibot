"""Controller module."""

import time

from pibot import motor
from pibot import ultrasound


class this:
    """Global variables."""
    state = "stop"


def init():

    motor.setup()
    ultrasound.setup()

    print("Pibot has been initialized.")


def operate():

    if this.state == "stop":
        motor.stopmotors()
        return

    controller()


def controller():

    dist = get_dist()
    dir = "forward"

    DIST_TH = 15
    DIST_TO_WALL = 70

    if dist > DIST_TO_WALL + DIST_TH:
        dir = "left"

    elif dist < DIST_TO_WALL - DIST_TH:
        dir = "right"

    else:
        dir = "forward"

    motor.set_dir(dir)
    print("Distance: " + str(dist) + " cm | Direction: " + str(dir))


def test():

    print("Performing controller test.")

    print("forward")
    motor.set_dir("forward")
    time.sleep(1)

    print("left")
    motor.set_dir("left")
    time.sleep(1)

    print("right")
    motor.set_dir("right")
    time.sleep(1)

    return "Controller test OK"


def set_state(state):

    if state not in ("start", "stop"):
        return "Cannot set state; invalid argument."

    else:
        this.state = state
        return "State set to: " + state


def get_dist():

    return ultrasound.measurement()


def get_motors():

    return "Left: " + str(motor.DutyCycleA) + "Right " + str(motor.DutyCycleB)
