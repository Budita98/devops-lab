from flask import Flask
import socket

from prometheus_client import Counter
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "flask_requests_total",
    "Cantidad total de requests recibidas"
)

@app.route("/")
def home():

    REQUEST_COUNT.inc()

    return f"""
    <h1>DevOps LabV6 ansible</h1>

    <p>Aplicacion Flask funcionando correctamente.</p>

    <p>Hostname: {socket.gethostname()}</p>
    """

@app.route("/metrics")
def metrics():

    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
