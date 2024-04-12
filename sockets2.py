from socket import *

def createServer():

    """
    Configura y ejecuta un servidor web básico.

    Esta función crea un servidor TCP/IP en el puerto 9000 de localhost.
    El servidor acepta conexiones entrantes y responde con un mensaje "Hello World"
    en formato HTML en cada solicitud HTTP recibida.

    Raises:
        KeyboardInterrupt: Si se interrumpe la ejecución del servidor (por ejemplo, con Ctrl+C),
                           el servidor se apaga limpiamente y muestra un mensaje de cierre.
        Exception:         Si ocurre cualquier otro error durante la ejecución del servidor,
                           se muestra un mensaje de error junto con detalles sobre la excepción.
    """
    # Configuración del servidor
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind(('localhost', 9000))
        server.listen(5)

        # Bucle principal del servidor
        while True:
            # Acepta una conexión entrante
            (clientsocket, address) = server.accept()

            # Recibe la solicitud del cliente
            request_data = (clientsocket.recv(5000).decode())
            request_lines = request_data.split('\n')

            # Imprime la primera línea de la solicitud (generalmente el método y la ruta HTTP)
            if len(request_lines) > 0:
                print(request_lines[0])

            # Construye la respuesta HTTP
            response_data = 'HTTP/1.1 200 OK\r\n'
            response_data += 'Content-Type: text/html; charset=utf-8\r\n'
            response_data += '\r\n'
            response_data += '<html><body>Hello World</body></html>\r\n\r\n'

            # Envía la respuesta al cliente
            clientsocket.sendall(response_data.encode())

            # Cierra la conexión de escritura del cliente
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as exc:
        print('Error:\n')
        print(exc)

# Ejecuta la función para iniciar el servidor
createServer()