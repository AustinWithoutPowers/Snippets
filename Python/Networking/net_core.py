import socket

# Leaving buffer size up to the calling party
def receive_data(conn, buffer_size):
	buffer = ''
	data = ''

	# This loop goes through until the full request has been parsed
	while True:
		buffer = conn.recv(buffer_size).decode()
		data += buffer

		if len(buffer) < buffer_size:
			break


	return data