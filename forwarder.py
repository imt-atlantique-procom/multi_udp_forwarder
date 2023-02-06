import socket
import argparse

from scheduler import RANDOM_SCHEDULER, schedule_func_from

BUFFER_SIZE = 65536
LOCALHOST_IP = "127.0.0.1"

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
parser.add_argument('-s', '--scheduler', choices=[RANDOM_SCHEDULER], default=RANDOM_SCHEDULER,
                    help='Port used to listen incoming packets')

args = parser.parse_args()

send_sockets = []
for address in args.address:
    ip, port = address.split(':')
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ip, int(port)))
    send_sockets.append(sock)

schedule_func = schedule_func_from(args.scheduler)

def receive_and_forward(receive_sock, dest_ip, dest_port):
    data, _addr = receive_sock.recvfrom(BUFFER_SIZE)
    send_sock = schedule_func(send_sockets)
    print(f"Sending {len(data)} bytes with {send_sock.getsockname()}")
    send_sock.sendto(data, (dest_ip, dest_port))

receive_port = args.port
dest_ip, dest_port = args.dest.split(':')
dest_port = int(dest_port)

receive_sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
receive_sock.bind((LOCALHOST_IP, receive_port))

print("Starting to listen on port " + str(receive_port) + " and forwarding to " + dest_ip + ":" + str(dest_port))
while True:
    receive_and_forward(receive_sock, dest_ip, dest_port)

