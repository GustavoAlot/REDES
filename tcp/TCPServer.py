from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()

while 1:
    message = ''
    sentence = connectionSocket.recv(1024).decode('utf-8')

    if sentence == 'ls' :
        message = " ".join(os.listdir())

    elif sentence == 'pwd' :
        message = os.getcwd()        

    elif sentence == 'scp' :
        message = 'digitou scp'

    elif sentence.split()[0] == 'cd'  :
        os.chdir( sentence.split()[1])
        message = os.getcwd() 

    else  :
        message = 'Comando inválido'

    connectionSocket.send(message.encode('utf-8'))


connectionSocket.close()