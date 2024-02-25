import socket
CHUNK_SIZE = 128
port = 19901
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((socket.gethostname(),port))
print(f"Started server on {s.getsockname()}")

while True:
    data , client = s.recvfrom(CHUNK_SIZE)
    decoded_data = data.decode('utf-8')
    print(decoded_data)

    sending = input("Reply :=>> ")
    s.sendto(sending.encode('utf-8'),client)