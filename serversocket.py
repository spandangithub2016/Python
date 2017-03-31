# a simple server socket
import socket
from time import ctime
# define socket address
TCP_IP = '0.0.0.0'  # consider all possible incoming IPs 
TCP_PORT = 5000  # port used for communicating with the client
BUFFER_SIZE = 1024  # buffer size used when receiving data
 
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created successfully.")
 
# bind socket
s.bind((TCP_IP, TCP_PORT))
 
# start listening
s.listen(5)
print ("Waiting for a connection...")
conn, addr = s.accept()
print( "Connected with " + addr[0] + " " + str(addr[1]))
  
# wait for connection
while True:
    
    dataIn = conn.recv(BUFFER_SIZE)
    if not dataIn:
        print("Spandan: By See u soon Server")
        break;     
    print("Spandan: "+ str(dataIn))
    dataOut = input("Server: ")
    message = dataOut.encode()
    conn.send(message)
s.close()
