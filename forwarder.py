import socket
import sys

send_sock_1 = socket.socket(socket.AF_INET,  # Internet
                       socket.SOCK_DGRAM)  # UDP
BUFFER_SIZE = 2048
def receive_and_forward(receive_sock, dest_ip, dest_port):
    data, _addr = receive_sock.recvfrom(BUFFER_SIZE)
    send_sock_1.sendto(data, (dest_ip, dest_port))

LOCALHOST_IP = "127.0.0.1"
receive_port = 0
dest_ip = "0"
dest_port = 0

if len(sys.argv) < 3:
    print("Error: invalid arguments")
    exit(1)
else:
    receive_port = int(sys.argv[1])
    dest_ip = sys.argv[2]
    dest_port = int(sys.argv[3])

receive_sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
receive_sock.bind((LOCALHOST_IP, receive_port))

print("Starting to listen on port " + str(receive_port) + " and forwarding to " + dest_ip + ":" + str(dest_port))
while True:
    receive_and_forward(receive_sock, dest_ip, dest_port)

