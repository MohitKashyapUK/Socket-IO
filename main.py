import eventlet
from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="eventlet")

@app.route("/")
def index():
    return "Hello!"

@socketio.on('connect')
def test_connect():
    emit('message', {'data': "Connected"})

@socketio.on("message")
def message(message):
    List = ["Hello!", "Hi!", "Sasriya kaal!", "Jai hind!"]
    for i in List:
        emit("message", {"data": i})
        time.sleep(2)

if __name__ == "__main__":
    socketio.run(app, server='eventlet')
