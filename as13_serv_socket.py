import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 18000
server_address = ('127.0.0.1', port)
server_socket.bind(server_address)
print(f'начинаю слушать порт {port}')
server_socket.listen()
print('после listen()')

try:
    connection, client_address = server_socket.accept()
    print(type(connection))
    print(f'Получен запрос на подключение от {client_address}!')
    buffer = b''
    while buffer[-1:] != b'\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'Получены данные: {data}')
            buffer += data
    print(f"Все данные: {buffer}")
    connection.sendall(b'response: ' + buffer)

finally:
    server_socket.close()
