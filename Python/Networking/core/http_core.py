HTTP_PORT = 80
HTTPS_PORT = 443
CRLF = '\r\n'

class request_packet:
    def __init__(self):
        pass

class response_packet:
    def __init__(self, status_line = '', headers = {}, body = ''):
        self.__status_line = status_line
        # This is object address, not a copy
        self.__headers = headers
        self.__body  = body

    # Getters and setters
    def get_status_line(self):
        return self.__status_line
    
    def get_headers(self):
        return self.__headers
    
    def get_body(self):
        return self.__body

    def set_status_line(self, new_status_line):
        self.__status_line = new_status_line
    
    def set_headers(self, new_headers):
        # This is object address, not a copy
        self.__headers = new_headers
    
    def add_header(self, new_header):
        if new_header[0] not in self.__headers.keys():
            self.__headers[new_header[0]] = new_header[1]
        else:
            # Update to add logging?
            print("Header already exists")
    
    def set_body(self, new_body):
        self.__body = new_body
    
    def __str__(self):
        response_string = self.__status_line + CRLF
        for header, header_data in self.__headers.items():
            response_string += header + ": " + header_data + CRLF
        response_string += CRLF + self.__body

        return response_string

    def __repr__(self):
        return str(self)