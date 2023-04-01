from flask import Flask
from flask_socketio import SocketIO, emit
#from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
#app.config['CORS_ALLOWED_ORIGINS'] = '*'
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="eventlet")
#, logger=True, engineio_logger=True)

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
    socketio.run(app, debug=True, host='0.0.0.0')
