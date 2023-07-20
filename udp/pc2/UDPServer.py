from socket import *
import os

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('Pronto para receber!')

while 1:
        modifiedMessage = ''

        (message, clientAddress) = serverSocket.recvfrom(2048)
        message = message.decode('utf-8')

        if message == 'ls' :
                modifiedMessage = " ".join(os.listdir())
                

        elif message == 'pwd' :
                modifiedMessage = os.getcwd()        



        elif message.split()[0] == 'scp' :
                
                ark = open(message.split()[1], 'rb')


                #---------
                data = ark.read(2048)
                while(data) :
                        serverSocket.sendto(data,clientAddress)
                        serverSocket.recv(2048)
                        data = ark.read(2048)
                ark.close()

                data = ''
                print('Acabou de enviar')
                serverSocket.sendto(data.encode('utf-8'),clientAddress)



        elif message.split()[0] == 'cd'  :

                if len(message.split()) !=  2 :
                        modifiedMessage = "Quantidade de argumentos invalida"

                        
                else :
                        try:
                                directory = message.split()[1].lstrip('/')
                                os.chdir(directory)
                                modifiedMessage = os.getcwd()
                        except:
                                modifiedMessage = "Arquivo nao existe"

        else  :
                modifiedMessage = 'Comando inválido '

        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)