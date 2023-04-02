from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="eventlet")

@app.route("/")
def index():
    return "Hello!"

@app.route("/check")
def check():
    import subprocess
    result = subprocess.run(["echo", "$PATH"], capture_output=True, text=True).stdout
    return result

@app.route("/run")
def run():
    import subprocess
    return subprocess.run(["ulimit", "-n", 65535], capture_output=True, text=True).stdout

@socketio.on('connect')
def test_connect(auth):
    emit('message', {'data': 'Connected'})

@socketio.on("message")
def message(message):
    emit(message)

if __name__ == "__main__":
    socketio.run(app)
