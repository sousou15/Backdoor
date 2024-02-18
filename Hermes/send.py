from flask import Flask, send_file

app = Flask(__name__)

@app.route('/descargar_hello_bat')
def descargar_hello_bat():
    try:
        return send_file('hello.bat', as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
