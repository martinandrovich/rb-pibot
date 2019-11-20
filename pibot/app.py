"""Application code."""
from pibot import server
from pibot import core


def run():
    """Complete the program."""
    # init server + commands table
    server_ = server.Server()
    server_.commands = {
        b'getdist': core.get_dist(),
        b'getmotors': core.get_motors(),
        b'start': core.set_state('start')
    }

    # init controller
    core.init()

    # main loop
    while True:
        server_.operate()
        core.operate()


if __name__ == '__main__':
    run()
