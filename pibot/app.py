"""Main (app) module."""

from pibot import server
from pibot import core


def run():

    # init server + commands table
    srvr = server.Server("10.126.14.58")
    srvr.cmds = {
        b"getdist":    (lambda: core.get_dist),
        b"getmotors":  (lambda: core.get_motors),
        b"start":      (lambda: core.set_state("start")),
        b"stop":       (lambda: core.set_state("stop")),
        b"test":       (lambda: core.test)
    }

    # init controller
    core.init()

    # main loop
    while True:
        srvr.operate()
        core.operate()


if __name__ == '__main__':
    run()
