import socket

def main():
    host = '192.168.1.138'  # Local
    port = 12345  # Puerto que utilizará el servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Esperando conexión...")
        conn, addr = s.accept()
        with conn:
            print('Conectado a:', addr)
            while True:
                command = input("Introduce un comando para enviar al cliente (exit para salir): ")
                if command.lower() == 'exit':
                    conn.sendall(b'exit')
                    break
                conn.sendall(command.encode())
                data = conn.recv(1024)
                try:
                    print(data.decode('utf-8'))
                except UnicodeDecodeError:
                    print(repr(data))

if __name__ == "__main__":
    main()
