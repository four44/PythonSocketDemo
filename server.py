import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
users = []


def broadcast(message): #send message to clients
    for client in clients:
        client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client) #if there is error in a client, remove it from the list.
            clients.remove(client)
            client.close()
            user = users[index]
            broadcast(f'{user} has left the chat room!'.encode('utf-8'))
            users.remove(user)
            break
# Main function to receive the clients connection


def receive():
    while True:
        print('Server is running..')
        client, address = server.accept()  #server gets clients when client get called and connected to server
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        user = client.recv(1024)
        users.append(user)
        clients.append(client)
        print(f'The user of this client is {user}'.encode('utf-8'))
        broadcast(f'{user} has connected '.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()