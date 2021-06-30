import threading, json


class MainThread(threading.Thread):
    def __init__(self, s, func, debug, byteSizeRecv):
        super().__init__()
        self.s = s
        self.func = func
        self.debug = debug
        self.byteSizeRecv = byteSizeRecv

    def run(self):
        while True:
            clientsocket, address = self.s.accept()
            if self.debug:
                print(f"Connected from {address}")

            try:
                msg = clientsocket.recv(self.byteSizeRecv)
                send = self.func(msg.decode("utf-8"))
                if send is not None:
                    self.s.send(send.encode('utf-8'))

            except Exception:
                raise Exception

