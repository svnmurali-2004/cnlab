import socket 
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port=socket.gethostname(),5000
server_socket.bind((host,port))
server_socket.listen(5)
print("Server is waiting for connection")
client_socket,addr=server_socket.accept()
print(f"Connection from {addr} has been established")
while True:
    client_message=client_socket.recv(1024).decode("ascii")
    if not client_message:
        break
    print(f"Client : {client_message}")
    server_message=input("Server : ")
    client_socket.send(server_message.encode("ascii"))
client_socket.close()
server_socket.close()