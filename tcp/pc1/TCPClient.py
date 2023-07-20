from socket import *

serverName = 'localhost'
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

serverName = input('Server name connect: ')
serverPort = int(input('Server port connect: '))

while True:

    sentence = input('Da um comando ae').encode('utf-8')
    
    if sentence.decode('utf-8') == 'break' :
        break


    if sentence.split()[0].decode('utf-8') == 'scp' :
        ark = open(sentence.split()[1].decode('utf-8'), 'wb')

        content = clientSocket.recv(1024)    
        while content:
            ark.write(content)
            content = clientSocket.recv(1024)
        ark.close()
        print('Acabou')


    else :
        clientSocket.send(sentence)


    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode('utf-8') + '\n')

clientSocket.close()
