import socket
import argparse

parser = argparse.ArgumentParser(
    prog='Multi UDP Forwarder',
    description='Forwards data from one udp socket to multiple sockets',
    epilog='Made by Franco Liberali')

parser.add_argument('-a', '--address', nargs='+', required=True,
                    help='Addresses to use as source for the forwarding in format ip:port')
parser.add_argument('-d', '--dest', required=True,
                    help='Destination address in format ip:port')
parser.add_argument('-p', '--port', required=True, type=int,
                    help='Port used to listen incoming packets')

args = parser.parse_args()

send_sock_1 = socket.socket(socket.AF_INET,  # Internet
                       socket.SOCK_DGRAM)  # UDP
BUFFER_SIZE = 2048
def receive_and_forward(receive_sock, dest_ip, dest_port):
    data, _addr = receive_sock.recvfrom(BUFFER_SIZE)
    send_sock_1.sendto(data, (dest_ip, dest_port))

LOCALHOST_IP = "127.0.0.1"
receive_port = args.port
dest_ip, dest_port = args.dest.split(':')

receive_sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
receive_sock.bind((LOCALHOST_IP, receive_port))

print("Starting to listen on port " + str(receive_port) + " and forwarding to " + dest_ip + ":" + str(dest_port))
while True:
    receive_and_forward(receive_sock, dest_ip, dest_port)

