import threading
from socket import *

alias = input('enter your name .. ')

client = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9000

client.connect((host, port))


def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(msg)
        except:
            print(" you left the chat room.")
            client.close()
            break


def client_send():
    while True:
        x = input("")
        message = f'{alias}: {x}'
        client.send(message.encode('utf-8'))

        if x == "bye":
            client.close()
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
