from vidgear.gears import NetGear
import socket

class ConnectionModule:
    def __init__(self, logging, clientAddress, port):
        self.logging = logging
        self.port = port
        self.is_connected = False
        self.client = None
        self.server_data = None
        if clientAddress == "auto":
            self.clientAddress = socket.gethostbyname(socket.gethostname())
        else:
            self.clientAddress = clientAddress

        self.establish_connection(self.clientAddress)

    def establish_connection(self, clientAddress):
        self.clientAddress = clientAddress
        self.client = NetGear(receive_mode=True, logging=self.logging, address=self.clientAddress, port=self.port)
        self.target_data = None