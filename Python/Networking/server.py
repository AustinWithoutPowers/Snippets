import socket

def server(server_addr):
  server_socket = socket.socket()
  server_socket.bind(server_addr)

  server_socket.listen()
  conn, addr = server_socket.accept()

  while True:
    req = conn.recv(1024).decode()
    if not req:
      break

    print('Client request >', req)

    res = input(' -> ').encode()
    if not res:
      break

    conn.sendall(res)
    
  server_socket.close()

server(('localhost', 8081))