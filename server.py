import socket

# server listens to everything happening on the port, when client and server both connected
# they'll be able to communicate and send data


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = ('', 5656)

socket.bind((host, port))  # associate socket to an address
socket.listen(5)  # the 5 will authorize 5 failed connections before server refuses other connections
print("Server Connected")

while True:  # make the server listen to the port
    conn, address = socket.accept()  # will have IP address and port (IP value 0 & port value 1)
    print("Listening")

    data = conn.recv(1024)  # data will be received by connection
    # then we decode the data
    socket = data.decode("utf8")
    # then we show(print) what the server got from the client
    print(data)

# when you create a socket and open a connection, you need to close them both

conn.close()
socket.close()
