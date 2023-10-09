from socket import *
from threading import *
from random import *
# konstant
serverPort = 13000



def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()     

    splittetText = sentence.split()                
    Text=''
    if (splittetText[0].lower() == 'addition'):
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{talx} +  {taly} = {(talx+taly)}'
    
    elif (splittetText[0].lower() == 'subtraction'):
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{talx} -  {taly} = {(talx-taly)}'
    
    elif (splittetText[0].lower() == 'random'):
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{randint(talx, taly)}'
    else:
        Text = f'Ugyldigt.{splittetText[0]}'

    clientSocket.send(Text.encode())
    clientSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))            
serverSocket.listen(1)
print('Klar', serverSocket)


while True:
    connectionSocket, addr = serverSocket.accept()
    print('Serveren connected', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()
