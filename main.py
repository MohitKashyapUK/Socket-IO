from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="eventlet")

@app.route("/")
def index():
    return "Hello!"

@socketio.on('connect')
def test_connect(auth):
    emit('message', {'data': 'Connected'})

@socketio.on("message")
def message(message):
    emit(message)

if __name__ == "__main__":
    socketio.run(app, host=0.0.0.0, port=5000)
