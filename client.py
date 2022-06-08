import socket
import threading
#taking username as input from user
username = input("Enter Username: ")
#creating new socket for client
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            #sending username to server
            if message == 'USER':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break

def write():
    while True:
        #taking messages as input
        message= f'{username}: {input("")}'
        client.send(message.encode('ascii'))

#starting receive thread to get messages from server
receive_thread = threading.Thread(target=receive)
receive_thread.start()
#starting write thread to send messages to server
write_thread = threading.Thread(target=write)
write_thread.start()