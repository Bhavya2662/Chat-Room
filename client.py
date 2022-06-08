import socket
import threading
username = input("Enter Username: ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
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
        message= f'{username}: {input("")}'
        client.send(message.encode('ascii'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()