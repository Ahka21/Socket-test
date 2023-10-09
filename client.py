from socket import *

serverName = 'localhost'
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
text = input('addition, subtraction eller random')



c = text.encode()
clientSocket.send(c)

textmodtaget = clientSocket.recv(1024)
cs = textmodtaget.decode()

print('Modtager: ', textmodtaget.decode()) 
clientSocket.close()