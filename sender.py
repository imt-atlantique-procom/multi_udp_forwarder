import socket

DEST_IP = "127.0.0.1"
DEST_PORT = 5005


print("UDP target IP: %s" % DEST_IP)
print("UDP target port: %s" % DEST_PORT)
  
sock_1 = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
message_1 = b"Hello, "

sock_2 = socket.socket(socket.AF_INET,  # Internet
                       socket.SOCK_DGRAM)  # UDP
message_2 = b"World!"

sock_1.sendto(message_1, (DEST_IP, DEST_PORT))
sock_2.sendto(message_2, (DEST_IP, DEST_PORT))
