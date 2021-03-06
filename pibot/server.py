"""Python server socket."""
import socket


class Server:
    """Server socket."""

    def __init__(self, host=socket.gethostname(), port=8080):
        """Construction."""
        self.port = port
        self.host = host
        self.cmds = {}
        print('Create socket')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Bind socket(host={}, port={})'.format(self.host, self.port))
        self.socket.bind((self.host, self.port))
        self.is_socket_connected = False
        self.socket.listen()
        self.socket.settimeout(0.1)

    def __del__(self):
        """Destruction."""
        self.socket.close()

    def listen(self):
        """Listen to socket, and parse cmds."""
        try:
            connection, address = self.socket.accept()
            print('Got a connection={}, address={}'.format(connection, address))
            connection.settimeout(0.1)
            with connection:
                while True:
                    msg = connection.recv(1024)
                    if msg:
                        response = msg + b' was called and returned:  ' + str(self.parse_cmd(msg)).encode('ascii') + b'\n'
                        connection.sendall(response)
                    else:
                        connection.close()
                        break

        except socket.timeout as e:
            raise e

    def operate(self):
        """Operation."""
        try:
            self.listen()
        except socket.timeout:
            pass

    def parse_cmd(self, cmd):
        """Lookup in dict, and call the cmd."""
        if cmd in self.cmds:
            return self.cmds[cmd]()
        else:
            return "Cant parse cmd"
