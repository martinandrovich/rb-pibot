#!/usr/bin/env python3

from pibot import server
from pibot import core

def run():
    
    # init server + commands table
    server_ = server.Server()
    server_.cmds = {
        b'getdist': core.get_dist,
        b'getmotors': core.get_motors,
        b'start': lambda: core.set_state('start'),
        b'stop': lambda: core.set_state('stop')
    }

    # init controller
    core.init()

    # main loop
    while True:
        server_.operate()
        core.operate()


if __name__ == '__main__':
    run()
