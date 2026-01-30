import socket
 
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('127.0.0.1', 9000))
my_socket.listen(1)
while True:
    print('ждём подключения')
    client, address = my_socket.accept()
    print('клиент подключился')
    while True:
        data = client.recv(1024)
        if data:
            print('клиент отправил: ', data.decode())
            client.send(f'ответ: {data.decode()}'.encode())
        else:
            break
    client.close()
    print('клиент отключился')
my_socket.close()