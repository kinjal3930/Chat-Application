# import socket
# import threading

# # Function to receive messages from server
# def receive_messages(client_socket):
#     while True:
#         try:
#             message = client_socket.recv(1024).decode()
#             print("\n" + message)
#         except:
#             # If receiving fails, assume server has closed connection
#             print("Server closed the connection")
#             client_socket.close()
#             break

# # Main function
# def main():
#     # Server configuration
#     host = "127.0.0.1"
#     port = 8080

#     # Create client socket
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Connect to server
#     client_socket.connect((host, port))

#     # Start a new thread to receive messages from server
#     receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
#     receive_thread.start()

#     print("Connected to server. Type 'bye' to quit.")

#     while True:
#         # Send message to server
#         message = input()
#         if message.lower() == "bye":
#             break
#         client_socket.send(message.encode())

#     client_socket.close()

# if __name__ == "__main__":
#     main()


#Client
import threading
import socket

alias = input('Choose an Name : ')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6000))

def clnt_recv():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=="alias?":
                client.send(alias.encode('utf-8'))
            
            else:
                print(message)
            
        except:
            print('Error!')
            client.close()
            break

def clnt_send():
    while True:
        message=f'{alias}:{input("")}'
        client.send(message.encode('utf-8'))

receive_thread=threading.Thread(target=clnt_recv)  
receive_thread.start()

send_thread=threading.Thread(target=clnt_send)
send_thread.start()