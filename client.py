import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost' # Get local machine name
port = 12345                # Reserve a port for your service.

try:
    s.connect((Host, port))
    print "Port {} is open on host {}".format(port, Host)
except:
    print "Connection failed"
print s.recv(1024)
s.close()  
