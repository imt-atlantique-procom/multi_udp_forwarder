import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

BUFFER_SIZE = 2048

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print("received message: %s" % data)