import socket
host,port=socket.gethostname(),5000
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))
print("Server is waiting for connection")
while True:
    client_message,client_address=server_socket.recvfrom(1024)
    if not client_message:
        break
    print(f"Client : {client_message.decode('ascii')}")
    server_message=input("Server : ")
    server_socket.sendto(server_message.encode("ascii"),client_address)
server_socket.close()