import socket
import subprocess
import os

def main():
    host = '127.0.0.1'
    port = 8000

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            print("Esperando conexión...")
            conn, addr = s.accept()
            print('Conectado a:', addr)

            while True:
                try:
                    command = conn.recv(1024).decode()
                    if not command:
                        print("Cliente desconectado.")
                        break
                    if command.lower() == 'exit':
                        output = "bye"
                    elif command.startswith('cd '):
                        directory = command.split(' ', 1)[1]
                        try:
                            os.chdir(directory)
                            output = f"Cambiado al directorio: {os.getcwd()}"
                        except Exception as e:
                            output = str(e)
                    else:
                        try:
                            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                        except Exception as e:
                            output = str(e).encode()

                    if isinstance(output, bytes):
                        try:
                            output = output.decode('utf-8')
                        except UnicodeDecodeError:
                            output = output.decode('latin-1')

                    conn.sendall(output.encode())
                except ConnectionResetError:
                    print("El cliente cerró la conexión inesperadamente.")
                    break
                except KeyboardInterrupt:
                    print("Saliendo del programa...")
                    break

if __name__ == "__main__":
    main()
