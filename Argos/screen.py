import requests
import pyautogui
import cv2
import numpy as np

# URL del servidor donde deseas enviar el video
url = 'http://192.168.1.138:3030/upload_video'  # Reemplaza 'tu_ip_servidor' y 'puerto' con la dirección y el puerto de tu servidor

# Configurar el tamaño de la pantalla
screen_size = (1920, 1080)  # Ajusta este tamaño según tu resolución de pantalla

# Configurar el archivo de salida de video
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, screen_size)

try:
    while True:
        # Capturar pantalla
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Escribir el frame en el archivo de salida de video
        out.write(frame)

        # Convertir el frame a bytes para enviarlo por la solicitud HTTP
        _, img_encoded = cv2.imencode('.png', frame)
        img_bytes = img_encoded.tobytes()

        # Realizar la solicitud HTTP POST para enviar el frame de vídeo
        response = requests.post(url, data=img_bytes)

        # Detener la grabación cuando se presiona 'q'
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Cerrar el archivo de salida de video
    out.release()
