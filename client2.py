import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # to be able to connect client needs the same info
host, port = ('localhost', 5656)  # can be either localhost or 127.0.0.1


try:
    socket.connect((host, port))
    print("Client connected")

    data = "I am the client"
    # need to encode the data
    data = data.encode("utf8")
    # after encode, we can send the data
    # can use send or sendall to send all the data
    socket.sendall(data)
    # client will send the data on the port 5656 through the network
    # if server doesn't get it, it will be lost


except:
    print("Connection to server failed")

finally:
    socket.close()