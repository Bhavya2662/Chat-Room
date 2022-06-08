import threading
import socket

#localhost
host = '127.0.0.1'
port = 9999
#creating socket for server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#binding server with our host and port
server.bind((host,port))
#starting server to listen
server.listen()
#creating lists for clients and usernames
clients=[]
usernames=[]

def broadcast(message):
    #sending message from server to all clients
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            #recveing message from client
            message=client.recv(1024)
            #broadcasting it to every client
            broadcast(message)
        except:
            #if client is not responding, remove that client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username=usernames[index]
            broadcast(f'{username} left the chat'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:

        client, address = server.accept()
        print('Connected with ',address)
        #asking client for username
        client.send('USER'.encode('ascii'))
        #getting username from client
        username = client.recv(1024).decode('ascii')
        #adding username and new client to list
        usernames.append(username)
        clients.append(client)

        print(f'Username of the client is {username}')
        broadcast(f'{username} joined the chat'.encode('ascii'))
        client.send("Connected to the server".encode('ascii'))
        #starting a new thread for handling client messages
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("Server is on")
receive()