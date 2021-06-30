import socket, json


class Main:
    def __init__(self, ip: str = "0.0.0.0", port: int = 1111, sendAndReceive: bool = False,
                 useDebugMessages: bool = True):
        """
        :param ip: (str) (defaults to 0.0.0.0) IP Address to connect to, your current device must have access to it
        :param port: (int) (defaults to 1111) Port number for connection
        :param sendAndReceive: (bool) (defaults to False) If server should send and receive 1 piece of data
        :param useDebugMessages: (bool) (defaults to True) if you want to see debug messages
        """
        self.port = port
        self.ip = ip
        self.sendAndReceive = sendAndReceive
        self.debug = useDebugMessages
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        if self.debug:
            print("Connecting to server")

        self.s.connect((self.ip, self.port))

        if self.debug:
            print(f"Connected to server {self.ip} with port {self.port}")

    def send(self, data: bytes):
        self.s.send(data)

        if self.sendAndReceive:
            msg = self.s.recv(1024)
            return msg.decode("utf-8")
