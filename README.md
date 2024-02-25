# Backdoor ES
Para exponerlo a internet redirigir con TCP no con HTTP. Ejemplo: ngrok tcp 8080. Estamos trabajando con sockets.

Las carpetas "build" y "dist" son para crear un ejecutable de nuestyro python script.

En NOTAS.txt salen algunos comandos que se pueden hacer. Podemos convertir el ejecutable en tarea y hacer que se ejecute cada x tiempo para volver a recuperar la conexión.
Podemos usar curl para junto con los servidores Hermes, Loki, Hestia.

Backdoor Maat: Concede acceso al cmd de los sistemas objetivo, facilitando la ejecución de comandos, manipulación de archivos y reconocimiento. Servidor. Puerto: 12345

MaatReverse: Establece una conexión inversa , permitiendo la comunicación desde el objetivo hasta el servidor del operador que en este caso es el cliente. Shell inverso.

Hestia: Crea una interfaz oculta para la recuperación segura de archivos del sistema objetivo, garantizando la extracción sigilosa de datos. Servidor. Puerto: 5000

Loki: Permite la descarga de archivos desde sistemas objetivo. Servidor. Puerto: 8000

Hermes: Inyecta archivos en sistemas objetivo, integrándolos sin problemas en directorios para uso futuro. Servidor. Puerto: 3030

Argos: Captura la actividad de la pantalla objetivo, proporcionando un archivo visual. Servidor. Puerto: 3030

# Backdoor EN
"To expose it to the internet, redirect with TCP not with HTTP. Example: ngrok tcp 8080. We are working with sockets.

The folders "build" and "dist" are for creating an executable of our Python script.

In NOTES.txt, there are some commands that can be executed. We can schedule the executable as a task to run at intervals to re-establish the connection.
We can use curl along with the Hermes, Loki, and Hestia servers.

Maat: Grants comprehensive access to target systems, facilitating command execution, file manipulation, and reconnaissance. Server. Port: 12345

MaatReverse: Establishes a covert reverse connection, enabling communication from the target to the operator's server without detection. Reverse shell.

Hestia: Creates a concealed interface for secure file retrieval from the target system, ensuring stealthy data extraction. Server. Port: 5000

Loki: Allows file downloads from target systems. Server. Port: 8000

Hermes: Injects files into target systems, seamlessly integrating them into directories for future use. Server. Port: 3030

Argos: Captures target screen activity, providing a visual file. Server. Port: 3030
