import socket

def client(server_addr):
  client_socket = socket.socket()
  client_socket.connect(server_addr)

  req = input(' -> ').encode()

  while req:
    client_socket.sendall(req)
    res = client_socket.recv(1024).decode()

    print('Server response >', res)

    req = input(' -> ').encode()
    
  client_socket.close()

client(('localhost', 8081))