import socket
host,port=socket.gethostname(),5000
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address=(host,port)

while True:
    message=input("Client : ")
    client_socket.sendto(message.encode("ascii"),server_address)
    if message.lower()=="exit":
        break
    server_message,server_address=client_socket.recvfrom(1024)
    print(f"Server : {server_message.decode('ascii')}")