from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)

@app.route("/")
def index():
    return "Hello!"

@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})

@socketio.on("message")
def message(message):
    emit(message)

if __name__ == "__main__":
    socketio.run(app, cors_allowed_origins='*', host='localhost', port=26543)
