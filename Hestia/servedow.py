from flask import Flask, send_file, request
import os

app = Flask(__name__)

# Ruta del archivo a servir
archivo_a_servir = 'archivo.txt'

# Ruta del archivo de registro
archivo_de_registro = 'registro.txt'

@app.route('/descargar_archivo')
def descargar_archivo():
    # Registra la IP que descargó el archivo
    ip = request.remote_addr
    registrar_descarga(ip)
    # Sirve el archivo para su descarga
    return send_file(archivo_a_servir, as_attachment=True)

def registrar_descarga(ip):
    # Registra la IP en el archivo de registro
    with open(archivo_de_registro, 'a') as f:
        f.write(f'IP: {ip}\n')

if __name__ == '__main__':
    # Inicia el servidor
    app.run(host='0.0.0.0')
