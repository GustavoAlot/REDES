from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
        modifiedMessage = ''
        (message, clientAddress) = serverSocket.recvfrom(2048)
        message = message.decode('utf-8')
        if message == 'ls' :
                modifiedMessage = " ".join(os.listdir())

        elif message == 'pwd' :
                modifiedMessage = os.getcwd()        

        elif message == 'scp' :
                modifiedMessage = 'digitou scp'

        elif message.split()[0] == 'cd'  :
                os.chdir( message.split()[1])
                modifiedMessage = os.getcwd() 

        else  :
                modifiedMessage = 'Comando inválido'

        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)