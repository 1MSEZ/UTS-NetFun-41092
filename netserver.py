# Import socket module
import socket
import sys          # In order to terminate the program 

# Bind the socket to server address and server port
serverPort = 8080
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive on', serverPort)

# Server should be up and running and listening to the incoming connections
while True:
	print ('Ready to serve...')
	
	# It sets up a new connection from the client
	connectionSocket, addr = serverSocket.accept()
	
	try:
		# Receives messages from the client
		message =  connectionSocket.recv(1024)
		filename = message.split()[1]
		file = open(filename[1:])
		outputdata = file.read()
		connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
 
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode("UTF-8"))
		connectionSocket.send(b"\r\n")
		connectionSocket.close()
		print("Message Successfully Sent")
		sys.exit()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send((b"HTTP/1.1 404 Not Found\r\n\r\n"))
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		# Close the client connection socket
		connectionSocket.close()
		print("404 Error Occured")
		sys.exit()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data  
