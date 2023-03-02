from socket import *
import sys
#The code I wrote  first parses the command-line arguments to get the server host, port number, and file name to request. 
# It then opens the specified file, reads its contents, and sends an HTTP GET request to the server using the socket library. 
# Finally, it prints the server's response and closes the socket.

#Task 2: Making a web client starts here:

# Parse command line arguments
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])#Since it is passed as a string, we need to convert it to an integer using the int() function.
filename = sys.argv[3]#This allows us to pass command-line arguments to the script when we run "python client.py serverhost serverport index.html"

# Read contents of file
with open(filename, 'r') as f: #creates a file object f and opens the file filename in read-only mode
#takes two arguments: 
# the first is the name of the file to open, 
# second is a string representing the mode in which to open the file
# the mode is 'r', which means "read mode"
    output = f.read() #reads the contents of the f file and assigns it to variable output


client_socket = socket(AF_INET, SOCK_STREAM)
# connects to the server at the specified IP address and port number
client_socket.connect((str(serverHost), int(serverPort)))

request = f"GET /{filename} HTTP/1.1\r\nHost: {serverHost}:{serverPort}\r\n\r\n"

# Send the HTTP GET request to the server, encoded as bytes.
client_socket.sendall(request.encode())

# Send the contents of the file to the server, encoded as bytes.
client_socket.send(output.encode())

response_message = client_socket.recv(1024) # receive response


# Print the response
while len(response_message) > 0:
    print("Response msg is " + response_message.decode()) # show in terminal
    response_message = client_socket.recv(1024)

# Close the socket
client_socket.close() # close the connection
