import socket
import random
import string
import time

DEST_IP = "127.0.0.1"
DEST_PORT = 8887
MSG_LEN = 10
TIME_BETWEEN_MSG = 2 # seconds

print("UDP target IP: %s" % DEST_IP)
print("UDP target port: %s" % DEST_PORT)

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET,  # Internet
                  socket.SOCK_DGRAM)  # UDP

while True:
    message = ''.join(random.choices(string.ascii_lowercase, k=MSG_LEN))
    s.sendto(message.encode('utf-8'), (DEST_IP, DEST_PORT))
    print(f"sent: {len(message)}, {message}")
    time.sleep(TIME_BETWEEN_MSG)
