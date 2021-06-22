import socket

BUFFER_SIZE = 1024

def receive_data(conn, addr):
  while True:
    buffer = conn.recv(BUFFER_SIZE).decode()
    if not buffer:
      return None
    print("here?!?")
    req = buffer
    while len(buffer) > BUFFER_SIZE - 1:
      print("a")
      buffer = conn.recv(BUFFER_SIZE).decode()
      if not buffer:
        return req
      req += buffer

def server(server_addr):
  server_socket = socket.socket()
  server_socket.bind(server_addr)

  server_socket.listen()
  conn, addr = server_socket.accept()

  req = receive_data(conn, addr)
  print('Client request >:', req)
  conn.sendall('200 OK'.encode())
    
  server_socket.close()

server(('localhost', 8081))