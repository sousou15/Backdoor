from flask import Flask, request
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    # Obtener los bytes de la imagen del cuerpo de la solicitud
    img_bytes = request.data
    
    # Convertir los bytes de la imagen a un array numpy
    nparr = np.frombuffer(img_bytes, np.uint8)
    
    # Decodificar la imagen
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Guardar la imagen (puedes ajustar el nombre y la ubicación del archivo según sea necesario)
    cv2.imwrite('received_frame.png', frame)

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)  # Reemplaza 'puerto' con el puerto en el que deseas ejecutar tu servidor Flask
