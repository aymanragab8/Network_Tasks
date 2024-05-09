from socket import *
s = socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port= 4000
s.connect((host,port))
print(" to end the session write 'bye' ")

while True:
    client_msg= input("client: ").encode('utf-8')
    
    msg_len = len(client_msg)
    
    if msg_len > 2048:
        z = msg_len // 2048 + 1

        for i in range(z):
            begin = i * 2048
            end = min((i + 1) * 2048, msg_len)
            s.send(client_msg[begin:end])

    else:
        s.send(client_msg)
    
    if client_msg.decode('utf-8') == "bye":
         break
    
    x=s.recv(2048)
    print("server:",x.decode('utf-8'))
    
s.close()