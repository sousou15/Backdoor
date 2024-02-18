from flask import Flask, send_file, request
import requests

app = Flask(__name__)

# Ruta del archivo a servir
archivo_a_servir = 'archivo.txt'

# Ruta del archivo de registro
archivo_de_registro = 'registro.txt'

def obtener_ip_publica():
    try:
        response = requests.get('https://httpbin.org/ip')
        data = response.json()
        return data['origin']
    except Exception as e:
        print(f"No se pudo obtener la IP pública: {e}")
        return None

@app.route('/descargar_archivo')
def descargar_archivo():
    # Registra la IP pública que descargó el archivo
    ip = obtener_ip_publica()
    if ip:
        registrar_descarga(ip)
    # Sirve el archivo para su descarga
    return send_file(archivo_a_servir, as_attachment=True)

def registrar_descarga(ip):
    # Registra la IP en el archivo de registro
    with open(archivo_de_registro, 'a') as f:
        f.write(f'IP: {ip}\n')

if __name__ == '__main__':
    # Inicia el servidor
    app.run(host='0.0.0.0', port=5000)
