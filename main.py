import eventlet
eventlet.monkey_patch()
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="eventlet")

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('message', { 'data': "Connected" })

@socketio.on("start")
def start():
    emit("message", { "data": "Starting!" }, broadcast=True)

    import subprocess
    output = subprocess.run(['su', '-'], capture_output=True).stdout.decode("utf-8")
    emit("message", {"data": output}, broadcast=True)

    output = subprocess.run(["apt-get", "update", "-y"]).stdout.decode("utf-8")
    emit("message", { "data": output }, broadcast=True)

    output = subprocess.run(["apt-get", "upgrade", "-y"], capture_output=True).stdout.decode("utf-8")
    emit("message", { "data": output }, broadcast=True)

    requirements = ['make', 'git', 'zlib1g-dev', 'libssl-dev', 'gperf', 'cmake', 'clang', 'libc++-dev', 'libc++abi-dev']
    for i in requirements:
        output = subprocess.run(['apt-get', 'install', i, '-y'], capture_output=True).stdout.decode("utf-8")
        emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['exit']).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['git', 'clone', '--recursive', 'https://github.com/tdlib/telegram-bot-api.git'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['cd', 'telegram-bot-api'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['rm', '-rf', 'build'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['mkdir', 'build'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['cd', 'build'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    compile = 'CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang CXX=/usr/bin/clang++ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..'.split()
    output = subprocess.run(compile, capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['cmake', '--build', '.', '--target', 'install'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['cd', '../..'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

    output = subprocess.run(['ls', '-l', 'telegram-bot-api/bin/telegram-bot-api*'], capture_output=True).stdout.decode("utf-8")
    emit('message', { 'data': output }, broadcast=True)

@socketio.on("message")
def message(message):
    List = ["Hello!", "Hi!", "Sasriya kaal!", "Jai hind!"]
    for i in List:
        emit("message", {"data": i}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, server='eventlet')
