from . import ServerBase, ClientBase

"""
Receive and Send Server Example:

import socket_utils

server = ServerBase(ip="0.0.0.0", port=1111, listenToRequestsAmount=5, useDebugMessages=True, receiveByteSize=1024)
server.run()

def on_receive_data(msg):
    data = msg
    if data == "Testing":
        return "Received"

server.on_receive_data(on_receive_data)
"""

"""
Receive and Send Client Example:

import socket_utils
client = ClientBase(ip="0.0.0.0", port=1111, sendAndReceive=True, useDebugMessages=True)
result = client.send("Testing")
if result == "Received":
    print('finished')

"""