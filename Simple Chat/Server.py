from socket import *
s = socket(AF_INET,SOCK_STREAM)
print("socket created")
host='127.0.0.1'
port= 4000
s.bind((host,port))
print("socket binded to ",port)
s.listen(5)
print("socket is listening")
c,addr = s.accept()
print('get connection from', addr)

while True:
    x=c.recv(2048)
    print("client:",x.decode('utf-8'))

    if x.decode('utf-8') == "bye" :
        break
        
    msg= input("server: ").encode('utf-8')

    l = len(msg)
    if l > 2048:
        x = l // 2048 + 1
        for i in range(x):
            begin = i * 2048
            end = min((i + 1) * 2048, l)
            s.send(msg[begin:end])
    else:
        c.send(msg)
       
c.close()