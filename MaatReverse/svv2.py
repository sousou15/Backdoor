import socket

def main():
    host = '192.168.1.149' #192.168.1.138'  # Cambia esto por la dirección IP del cliente
    port = 8000  # Puerto que utilizará el servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            command = input("Introduce un comando para enviar al cliente (exit para salir): ")
            if command.lower() == 'exit':
                s.sendall(b'exit')
                break
            s.sendall(command.encode())
            data = s.recv(1024)
            try:
                print(data.decode('utf-8'))
            except UnicodeDecodeError:
                print(repr(data))

if __name__ == "__main__":
    main()
