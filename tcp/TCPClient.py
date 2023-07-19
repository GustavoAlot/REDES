from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input lowercase sentence: ').encode('utf-8')
    if message.decode('utf-8') == 'break' :
        break
    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode('utf-8') + '\n')

clientSocket.close()
