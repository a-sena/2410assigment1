#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 9000
recvBuffer = 1024
serverHost=''127.0.0.1''
#Prepare a sever socket
#Write your code here
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	print('Ready to serve...')
	conn, addr = serverSocket.accept()
	try:
		#Write your code here

		#End of your code
		message = conn.recv(recvBuffer) 
		print (message,'::',message.split()[0],':',message.split()[1])
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		f.close() 

		#Send one HTTP header line into socket
		#Write your code here
		response = 'HTTP/1.0 200 OK\n\n' + outputdata
		conn.sendall(response.encode())
		#End of your code

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			conn.send(outputdata[i].encode()) 
		conn.send("\r\n".encode())
		conn.close()


	except IOError:
		#Send response message for file not found
    	#Write your code here
		conn.send("HTTP/1.1 404 Not Found\r\n".encode())
		conn.send("Content-Type: text/html\r\n".encode())
		conn.send("\r\n".encode())
		conn.send("<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())

    	#End of your code
		
		#Close client socket
        
        #Write your code here
		conn.close()
		#End of your code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
