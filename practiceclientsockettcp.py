import socket 
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port=socket.gethostname(),5000
client_socket.connect((host,port))

while True:

    client_message=input("Client : ")
    client_socket.send(client_message.encode("ascii"))
    if client_message.lower()=="exit":
        break
    server_message=client_socket.recv(1024).decode("ascii")
    print(f"Server : {server_message}")
client_socket.close()
