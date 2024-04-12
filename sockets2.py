from socket import *

def createServer():
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind(('localhost', 9000))  # Corrected variable name
        server.listen(5)
        while True:  # Changed while(1) to while True
            (clientsocket, address) = server.accept()  # Corrected variable name
            rd = (clientsocket.recv(5000).decode())
            pieces = rd.split('\n')
            if len(pieces) > 0:
                print(pieces[0])
            data = 'HTTP/1.1 200 OK\r\n'  #  HTTP header syntax
            data += 'Content-Type: text/html; charset=utf-8\r\n'  # variable name
            data += '\r\n'
            data += '<html><body>Hello World</body></html>\r\n\r\n'  # HTTP body formatting
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)  # variable name

    except KeyboardInterrupt:  #  syntax for exception handling
        print('\nShutting down...\n')
    except Exception as exc:
        print('Error:\n')
        print(exc)

createServer()
