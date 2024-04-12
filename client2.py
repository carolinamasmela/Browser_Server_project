import urllib.request #permite abrir conexiones a recursos en línea


# Abrir una conexión al recurso en línea (en este caso, un archivo de texto llamado 'romeo.txt' en el servidor local)
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

# Iterar sobre cada línea del archivo remoto
for line in fhand:
    # Decodificar la línea de bytes a cadena y eliminar espacios en blanco adicionales alrededor
    decoded_line = line.decode().strip()
    # Imprimir la línea decodificada
    print(decoded_line)

