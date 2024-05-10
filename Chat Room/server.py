import threading
from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9000
s.bind((host, port))
s.listen()

clients = []
aliases = []
clients_number = 0

def broadcast_msg(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def handle_client(client):
    global clients_number
    while True:
        try:
            msg = client.recv(1024)
            broadcast_msg(msg, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast_msg(f'{alias} has left the chat room!'.encode('utf-8'), client)
            aliases.remove(alias)
            clients_number -= 1
            try:
                 if clients_number == 0:

                    print("chat is terminated") #
                    s.close()
            except:
                print("123")
            break

def receive_msg():
    global clients_number
    while True:
        print("server is listening...")
        print("to leave the chat , write bye ")
        client, addr = s.accept()
        clients_number += 1
        print(f'client {str(addr)} enter the room')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'the name of this client is {alias}'.encode('utf-8'))
        broadcast_msg(f'{alias} has connected to the chat room'.encode('utf-8'), client)
        client.send('you are connected to the room ..'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_msg()
