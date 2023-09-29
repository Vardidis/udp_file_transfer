from socket import *
import sys

hostname = sys.argv[1]
port = sys.argv[2]
command = sys.argv[3]
file = sys.argv[4] or None

serverName = hostname
serverPort = int(port)
clientSocket = socket(AF_INET, SOCK_DGRAM)

if command == 'get':

    if file == 'server' or file == 'client':
        clientSocket.sendto(bytes(command+' '+file, 'utf-8'), (serverName, serverPort))
    
    response, serverAddress = clientSocket.recvfrom(15000)
    with open(file+'.py', 'wb') as f:
        f.write(response)

# dirs = os.scandir('C://')
# aux = []
# for i in dirs:
#     aux.append(i.name)
# lis = bytearray(bytes(aux[0]+',', 'utf-8'))
# for i in aux[1:-1]:
#     lis.extend(bytes(i+',', 'utf-8'))
# lis.extend(bytes(aux[-1], 'utf-8'))
# clientSocket.sendto(lis,(serverName, serverPort))
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print(bytes.decode(modifiedMessage))

# while True:
#     clientSocket.sendto(b'',(serverName, serverPort))
#     com, serverAddress = clientSocket.recvfrom(2048)
#     if com.decode() == 'x':
#         break

#     if com.decode().startswith('get'):
#         aux = com.decode().split(' ')
#         file = None
#         with open(aux[1], 'rb') as f:
#             file = f.read()
#         clientSocket.sendto(file, (serverName, serverPort))
#         continue

#     if com.decode().startswith('dir'):
#         aux = com.decode().split(' ')
#         dirs = os.scandir(aux[1])
#         aux = []
#         for i in dirs:
#             aux.append(i.name)
#         ls = bytearray(bytes(aux[0]+',', 'utf-8'))
#         for i in aux[1:-1:]:
#             ls.extend(bytes(i+',', 'utf-8'))
#         ls.extend(bytes(aux[-1], 'utf-8'))
#         clientSocket.sendto(ls, (serverName, serverPort))
#         continue

#     if com.decode() == 't':
#         break
#     os.system(com.decode())

clientSocket.close()