from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)



while True: 

    message = input('Da um comando ae: ').encode('utf-8')
    
    if message.decode('utf-8') == 'break' :
        break
    clientSocket.sendto(message,(serverName, serverPort))



    if message.split()[0].decode('utf-8') == 'scp' :
        ark = open(message.split()[1].decode('utf-8'), 'wb')

        content, serverAddress = clientSocket.recvfrom(2048)    
        while content:
            ark.write(content)
            content, serverAddress = clientSocket.recvfrom(2048)
        ark.close()
        print('Acabou')





    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8')+ '\n')

clientSocket.close()



