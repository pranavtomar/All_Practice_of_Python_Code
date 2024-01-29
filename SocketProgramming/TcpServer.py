#How to write tcp server program with send the data to the client and recieve data from the client
#Build the python socket server
import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)

while True:
    print("Server waiting for connection")
    client_socket,addr=server_socket.accept()  #return 1.new socket object representing the connection, 2.tuple holding the address of the client
    print("client connected from ",addr)
    data=client_socket.recv(1024)
    if not data or data.decode('utf-8')=='END':
        break
    print("recieved from client : %s" %data.decode("utf-8"))
    try:
        client_socket.send(bytes('Hey client','utf-8'))
    except:
        print("Exited by the user")
    client_socket.close()
server_socket()


