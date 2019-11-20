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

    ctrl_threshold()


def ctrl_simple():

    dist = get_dist()
    dir = "right"

    if dist > 10:
        dir = "right"

    else:
        dir = "left"

    # call daniel's methods

    #msg = f"Distance: {dist} cm | Direction: {dir}"
    #print(msg)

def ctrl_threshold():

    dist = get_dist()
    dir = "forward"

    DIST_TH = 50
    DIST_TO_WALL = 70

    if dist > DIST_TO_WALL + 15:
        dir = "left"

    elif dist < DIST_TO_WALL - 15:
        dir = "right"

    else:
        dir = "forward"
    
    motor.set_dir(dir)
    print(dir)

    #msg = f"Distance: {dist} cm | Direction: {dir}"
    #print(msg)


def set_state(state):

    if state not in("start", "stop"):
        return "Cannot set state; invalid argument."

    else:
        this.state = state
        return "State set to: " + state


def get_dist():
    return ultrasound.measurement()

def get_motors():
    return "Left motor: " + str(motor.DutyCycleA) + "Right motor: " + str(motor.DutyCycleB)
