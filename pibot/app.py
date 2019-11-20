# import server
from pibot import core

def run():

	# hello
	print("Hello World!")

	# init server + commands table
	# server.init()
	# server.commands = { 
	# 	'getdist':   core.get_dist(),
	# 	'getmotors': core.get_motors(),
	# 	'start':	 core.set_state('start')
	# }

	# init controller
	core.init()

	# main loop
	while True:
		# server.operate()
		core.operate()

if __name__ == '__main__':
	run()