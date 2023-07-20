from socket import *
import os
serverPort = 12008
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


    elif sentence.split()[0] == 'scp' :
        ark = open(sentence.split()[1], 'rb')

        data = ark.read(1024)
        while(data) :
                connectionSocket.send(data)
                data = ark.read(1024)
        ark.close

        data = ''
        print('Acabou de enviar')
        connectionSocket.send(data.encode('utf-8'))
    

    elif sentence.split()[0] == 'cd'  :

        if len(sentence.split()) !=  2 :
            message = "Quantidade de argumentos invalida"

                        
        else :
            directory = sentence.split()[1].lstrip('/')
            os.chdir(directory)
            message = os.getcwd()

    elif sentence == 'break' :
        connectionSocket.close()

    else  :
        message = 'Comando inválido'

    connectionSocket.send(message.encode('utf-8'))

   

connectionSocket.close()