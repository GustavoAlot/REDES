from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)



while True: 

    message = input('Da um comando ae: ').encode('utf-8')
    if message.decode('utf-8') == 'break' :
        break
    clientSocket.sendto(message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8')+ '\n')

clientSocket.close()

