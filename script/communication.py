import requests
#from socketio_client import SocketIO, LoggingNamespace
import sys
import json
from datetime import datetime


class sender():
    def __init__(self, port=3001):

        self.url = "http://localhost:3001"
        self.headers = {
            'Content-type': 'application/json', 'Accept': 'text/plain'}

    def send(self, params):
        print("params:", params)
        requests.post(self.url, data=json.dumps(params), headers=self.headers)
        print("sended")



if __name__ == '__main__':
    a = sender()
    a.send({'msg': 'a', 'r': 'b'})