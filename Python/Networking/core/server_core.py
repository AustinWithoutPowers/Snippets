import socket
import net_core

BUFFER_SIZE = 1024
    
# Main function
def server(server_addr):
  # Make and bind socket
  server_socket = socket.socket()
  server_socket.bind(server_addr)

  # Listen and accept requests
  server_socket.listen()
  conn, addr = server_socket.accept()
  print('Connection coming from %s...' % addr[0])

  # This loop goes sends back the response and waits for the next request
  while True:
    req = net_core.receive_data(conn, BUFFER_SIZE)

    # Quitely closes the server socket if client closes
    # socket BEFORE attempting to send a response...
    if not req:
      break
    
    print('Client request >:', req)
    conn.sendall('200 OK'.encode())
    
  server_socket.close()

server(('localhost', 8081))