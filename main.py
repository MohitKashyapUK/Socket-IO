from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route("/")
def index():
    return "Hello!"

@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': f'Connected {auth}'})

@socketio.on("message")
def message(message):
    emit(message)

if __name__ == "__main__":
    socketio.run(app)
