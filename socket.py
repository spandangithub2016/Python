# a simple client socket
import socket
from time import ctime
# define socket address
TCP_IP = '127.0.0.1'  # ip of the server we want to connect to
TCP_PORT = 5000  # port used for communicating with the server
BUFFER_SIZE = 1024  # buffer size used when receiving data
 
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created successfully.")
 
# connect to server
s.connect((TCP_IP, TCP_PORT))
print ("Established connection with the server.")
message=""
dataOut="hello server"
while(message != 'stop'):

    message = dataOut.encode()
    s.send(message)

    dataIn = s.recv(BUFFER_SIZE)
    print("server :"+str(dataIn))

    dataOut = input("Spandan: ")
if(message=="stop"):
    print("Spandan: By See u soon Server")
    message = dataOut.encode()
    s.send(message)
    s.close()
s.close()

