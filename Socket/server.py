# import socket
# import threading

# # Function to handle client connections
# def handle_client(client_socket, add):
#     print(f"Accepted connection from {add}")

#     while True:
#         # Receive message from client
#         try:
#             message = client_socket.recv(1024).decode()
#             if not message:
#                 print(f"Connection with {add} closed")
#                 break
#             print(f"Received from {add}: {message}")
            
#             # Broadcast message to all connected clients
#             broadcast(message, client_socket)
#         except ConnectionResetError:
#             print(f"Connection with {add} closed unexpectedly")
#             break
    
#     client_socket.close()

# # Function to broadcast message to all clients
# def broadcast(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 client.send(message.encode())
#             except:
#                 # If sending fails, assume client has disconnected
#                 client.close()
#                 remove(client)

# # Function to remove client from list of clients
# def remove(client):
#     if client in clients:
#         clients.remove(client)

# # Main function
# def main():
#     # Server configuration
#     host = "127.0.0.1"
#     port = 8080

#     # Create server socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Bind server socket to host and port
#     server_socket.bind((host, port))

#     # Start listening for connections
#     server_socket.listen()

#     print("Server listening on port", port)

#     while True:
#         # Accept incoming connection
#         client_socket, add = server_socket.accept()
        
#         # Add client socket to list of clients
#         clients.append(client_socket)

#         # Start a new thread to handle client communication
#         client_thread = threading.Thread(target=handle_client, args=(client_socket, add))
#         client_thread.start()

# # List to keep track of connected clients
# clients = []

# if __name__ == "__main__":
#     main()


#Server

import threading
import socket
host ='127.0.0.1'
port=6000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
aliases=[]

def broadcast(message):
    for client in clients:
        client.send(message)


def handleclt(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            alias=aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    while True:
        print('Server is Running and Listening.....')
        client,address=server.accept()
        print(f'Connection is Established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias=client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        thread=threading.Thread(target=handleclt,args=(client,))
        thread.start()

if __name__=="__main__":
    receive()