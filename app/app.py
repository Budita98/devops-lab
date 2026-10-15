from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>DevOps Lab</h1>
    <p>Aplicacion Flask funcionando correctamente.</p>
    <p>Hostname: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
