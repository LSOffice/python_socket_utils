import socket, json
from .threads import main as threadm


class Main:
    def __init__(self, ip: str = "0.0.0.0", port: int = 1111, listenToRequestsAmount: int = 5,
                 useDebugMessages: bool = True, receiveByteSize: int = 1024):
        """
        :param ip: (str) (defaults to 0.0.0.0) IP Address to connect to, your current device must have access to it
        :param port: (int) (defaults to 1111) Port number for connection
        :param listenToRequestsAmount: (int) (defaults to 5) How many requests you want to listen to at once (depends on
        server capacity)
        :param useDebugMessages: (bool) (defaults to True) if you want to see debug messages
        :param receiveByteSize: (int) (defaults to 1024) Message maximum byte size
        """
        self.port = port
        self.ip = ip
        self.listenAmount = listenToRequestsAmount
        self.debug = useDebugMessages
        self.byteSizeRecv = receiveByteSize
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        if self.debug:
            print("Started setup process")

        self.s.bind((self.ip, self.port))
        if self.debug:
            print(f"Bound server to ip {self.ip} and port {self.port}")

        self.s.listen(self.listenAmount)
        if self.debug:
            print(f"Listening to {self.listenAmount} request(s)")

    def on_receive_data(self, function):
        thr = threadm.MainThread(self.s, function, self.debug, self.byteSizeRecv)
        thr.run()
