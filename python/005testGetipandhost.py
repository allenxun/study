import socket
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
#myserv = socket.getservbyname(myname)
print myname,myaddr,socket.__dict__
#myserv
