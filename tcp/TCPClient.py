from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('EEEEEEEEEEEEEescreve algo ae ').encode('utf-8')
    if sentence.decode('utf-8') == 'break' :
        break
    clientSocket.send(sentence)

    if sentence.split()[0].decode('utf-8') == 'scp' :
        ark = open(sentence.split()[1].decode('utf-8'), 'wb')

        content, serverAddress = clientSocket.recvfrom(1024)    
        while content:
            ark.write(content)
            content, serverAddress = clientSocket.recvfrom(1024)
        ark.close()
        print('Acabou')

    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode('utf-8') + '\n')

clientSocket.close()
