from socket import *
import datetime
import threading


serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 9000
recvBuffer = 1024
serverHost='158.36.145.211'
#Prepare a sever socket
#Write your code here
serverSocket.bind(('', serverPort))
serverSocket.listen(1)




#I create a handle_client function. It will  handle incoming client connections. 
# The function takes two arguments: conn, which is a socket object representing 
# the client connection, and addr, which is the client's address.
def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.".encode())
	while True:
	
		try:
			
			message = conn.recv(recvBuffer) #The server waits for a message/HTTP request from the client
			# I added a check to the while loop in handle_client to break the loop
			#  if message is empty, indicating that the client has disconnected.
			if not message:
				print(f"[DISCONNECTED] {addr} disconnected.")
				break
			print (message,'::',message.split()[0],':',message.split()[1])
			filename = message.split()[1].decode('utf-8')
			f = open(filename[1:])
			outputdata = f.read()
			print (outputdata) 

				

			#Send one HTTP header line into socket
			#Write your code here
			conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n".encode())
			#End of your code

			#Send the content of the requested file to the client 
			for i in range(0, len(outputdata)):
				conn.send(outputdata[i].encode()) 
			conn.send("\r\n".encode())
			conn.close()
			break #the entire file content is sent to the client before the connection is closed

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
			break
#The start function is defined to listen for new client connections and spawn a new thread to handle each connection.
def start():
    serverSocket.listen() # #we are now listening for new connection
    print(f"[LISTENING] Server is listening on {serverHost}:{serverPort}")
     #we are going to start a new thread which is equal to handle client, so a thread of function handle_client
        #and handle_client will handle all of the communicition between the clients and server
	
    while True:
        conn, addr = serverSocket.accept() #accept a new client connection
        print(f"[NEW CONNECTION] {addr} connected")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
#print amount of active connections currently
#when a new connection occurs, we are going to pass this connection "conn, addr=server.accept() to handle_clients 
#will give handle_clients "target is handle_clients"
#arguments are what arguments we are passing to the function, so in this case conn and addr
         
print("[STARTING] Server is starting...")
start()
        #function start meant to simply handle new connection and kind of disturbite those to where they need to go 
        #whereas function handle_client will  handle individuall connection between one server and one client

# Kilden som ble brukt for å kunne løse denne oppgaven er:
# https://www.youtube.com/watch?v=3QiPPX-KeSc