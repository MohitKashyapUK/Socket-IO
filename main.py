from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(
    app, 
    logger=True, 
    engineio_logger=True, 
    reconnect=True, 
    reconnect_timeout=5, 
    ping_timeout=120, 
    cors_allowed_origins='*', 
    async_mode="eventlet"
)

@app.route("/")
def index():
    return "Hello!"

@socketio.on('connect')
def test_connect(auth):
    emit('message', {'data': 'Connected'})

@socketio.on("message")
def message(message):
    emit("message",message)

if __name__ == "__main__":
    socketio.run(app, server='eventlet')
