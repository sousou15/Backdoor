import socket

def main():
    host = '127.0.0.1'  
    port = 8080  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        target_ip = s.recv(1024)
        print('Conectado a:', port, ': ', target_ip)

        while True:
            command = input("Introduce un comando para enviar al servidor (exit para salir): ")

            if command.lower() == 'exit':
                s.sendall(b'exit')
                break
            if not command:  
                print("Comando no especificado")
                continue

            s.sendall(command.encode())
                
            try:
                data = s.recv(1024)
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
