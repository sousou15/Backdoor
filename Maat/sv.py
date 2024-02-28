import socket

def main():
    host = '127.0.0.1'  # Cambia esto por la dirección IP de tu cliente
    port = 8080  # Puerto que utilizará el servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Esperando conexión...")
        conn, addr = s.accept()
        conn.settimeout(10)
        with conn:
            print('Conectado a:', addr)
            while True:
                command = input("Introduce un comando para enviar al cliente (exit para salir): ")
                if command.lower() == 'exit':
                    conn.sendall(b'exit')
                    break
                if not command:  # Verifica si command es None o una cadena vacía
                    print("Comando no especificado")
                conn.sendall(command.encode())
                
                try:
                    data = conn.recv(1024)
                    if not data:
                        continue
                    print(data.decode('utf-8'))
                except socket.timeout:
                    print("Tiempo de espera agotado.")
                    continue  # Continuar con el bucle para recibir más comandos
                except UnicodeDecodeError:
                    print(repr(data))

if __name__ == "__main__":
    main()
