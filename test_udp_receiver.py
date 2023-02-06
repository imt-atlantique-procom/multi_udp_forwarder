import socket

BUFFER_SIZE = 65536

UDP_IP = "127.0.0.1"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print("received message: %d, %s from %s" % (len(data), data, addr))