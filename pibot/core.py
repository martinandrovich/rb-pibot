"""Core functions."""
import sys
this = sys.modules[__name__]
this.state = "stop"


def init():
    print("Pibot has been initialized.")

def operate():

    if this.state == "stop":
        return

    print("Hello World!")

def set_state(state):
    """Set global state."""
    if state != ("start" or "stop"):
        return print("Cannot set state, invalid argument.")

    else:
        this.state = state
        return "State set to: " + state

def get_dist():
    return 69

def get_motors():
    return "Left motor: " + str(420) + "Right motor: " + str(6969)