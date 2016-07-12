import socket
s=socket.socket()
host="localhost"
port=12345
s.bind((host,port))
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()
