from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('message', { 'data': "Connected" })

@socketio.on("start")
def start(message):
    emit("message", { "data": "Starting!" }, broadcast=True)
    try:
        import subprocess
        output = subprocess.run(["uname", "-a"], capture_output=True).stdout.decode("utf-8")
        emit("message", {"data": output}, broadcast=True)
        commands = [
            "apt-get update",
            "apt-get upgrade",
            "apt-get install -y make git zlib1g-dev libssl-dev gperf cmake clang-10 libc++-dev libc++abi-dev",
            "git clone --recursive https://github.com/tdlib/telegram-bot-api.git",
            "cd telegram-bot-api",
            "rm -rf build",
            "mkdir build",
            "cd build",
            'CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang-10 CXX=/usr/bin/clang++-10 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..',
            "cmake --build . --target install",
            "cd ../..",
            "ls -l telegram-bot-api/bin/telegram-bot-api*"
        ]
        for i in commands:
            try:
                x = i.split()
                outputs = subprocess.run(x, capture_output=True).stdout.decode("utf-8")
                emit("message", { "data": f"{i}\n{outputs}" }, broadcast=True)
                print(outputs)
            except Exception as e:
                emit("message", { "data": f"Loop Error occured: {e}" })
        emit("message", { "data": "Completed!" })
    except Exception as e:
        emit("message", { "data": f"Error occured: {e}" })

@socketio.on("message")
def message(message):
    List = ["Hello!", "Hi!", "Sasriya kaal!", "Jai hind!"]
    for i in List:
        emit("message", {"data": i}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
