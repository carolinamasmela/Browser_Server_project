import socket  


# Crea un nuevo socket utilizando IPv4 y TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establece una conexión al servidor en la dirección IP 127.0.0.1 y el puerto 9000
mysock.connect(('127.0.0.1', 9000))

# Crea una solicitud GET HTTP para obtener el archivo romeo.txt del servidor
cmd = 'GET http://127.0.0.1/romeo.txt/1.0\r\n\r\n'.encode()

# Envía la solicitud codificada al servidor
mysock.send(cmd)

# Bucle para recibir y mostrar los datos del servidor
while True:
    data = mysock.recv(512)  # Recibe hasta 512 bytes de datos del servidor
    if len(data) < 1:  # Si no hay datos recibidos, sale del bucle
        break
    print(data.decode(), end='')  # Decodifica los datos y los muestra en la consola

# Cierra el socket, liberando los recursos y terminando la conexión
mysock.close()

