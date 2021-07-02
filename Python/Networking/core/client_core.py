import socket
import net_core

BUFFER_SIZE = 1024

# Main function
def client(server_addr):
  client_socket = socket.socket()
  client_socket.connect(server_addr)

  while True:
    req = input(' -> ').encode()
    if not req:
      break
    
    client_socket.sendall(req)

    res = net_core.receive_data(client_socket, BUFFER_SIZE)
    print('Server response >', res)
    
  client_socket.close()

client(('www.google.com', 443))