from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No se encontró el archivo en la solicitud', 400
    
    file = request.files['file']
    file.save(file.filename)
    
    return 'Archivo recibido con éxito', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # El servidor estará escuchando en todas las interfaces en el puerto 12345
