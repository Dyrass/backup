import socket
CHUNK_SIZE = 128
port = 19901
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


host = socket.gethostname()

while True:
    s.connect((host,port))
    message = input("Msg :=>> ")
    s.send(message.encode('utf-8'))

    # recieved
    recieved = s.recv(CHUNK_SIZE)
    print(recieved.decode('utf-8'))
    