from socket import *
#serverName = 'localhost'
#serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)


serverName = input('Server name connect: ')
serverPort = int(input('Server port connect: '))
while True: 

    message = input('Da um comando ae: ').encode('utf-8')
    
    if message.decode('utf-8') == 'break' :
        break
    




    if message.split()[0].decode('utf-8') == 'scp' :
        ark = open(message.split()[1].decode('utf-8'), 'wb')

        #-------
        clientSocket.sendto(message,(serverName, serverPort))
        content, serverAddress = clientSocket.recvfrom(2048)

        while content:
            ark.write(content)
            clientSocket.sendto(''.encode(),(serverName,serverPort))
            content, serverAddress = clientSocket.recvfrom(2048)
        ark.close()
        print('Acabou')

    else :
        clientSocket.sendto(message,(serverName, serverPort))





    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8')+ '\n')

clientSocket.close()



