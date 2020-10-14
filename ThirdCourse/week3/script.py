import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

text = list()
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    text.append(data.decode())

mysock.close()
for line in text:
    print(line)
