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
    """import os
    os.chdir("/opt/render/project/src")
    import requests
    url = "https://designative-propert.000webhostapp.com/my.sh"
    file = requests.get(url)
    with open("my.sh") as f:
        f.write(file.content)
    result = subprocess.run(["/bin/bash", "my.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    emit("message", { "data": result.stdout.decode() })
    emit("message", { "data": result.stderr.decode() })
    token = os.getenv("TOKEN")
    url = f"http://localhost:8081/bot{token}/getMe"
    res = requests.get(url)
    emit("message", { "data": res.text })"""
    
    
    
    
    try:
        import subprocess
        output = subprocess.run(["uname", "-a"], capture_output=True).stdout.decode("utf-8")
        emit("message", {"data": output}, broadcast=True)
        commands = [
            "apt-get update",
            "apt-get upgrade",
            "make git zlib1g-dev libssl-dev gperf cmake clang-10 libc++-dev libc++abi-dev",
            "git clone --recursive https://github.com/tdlib/telegram-bot-api.git",
            "cd telegram-bot-api",
            "rm -rf build",
            "mkdir build",
            "cd build",
            #'CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang-10 CXX=/usr/bin/clang++-10 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. -DCMAKE_CXX_FLAGS="-stdlib=libc++" ..',
            'CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang-10 CXX=/usr/bin/clang++-10 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..',
            "cmake --build . --target install",
            "cd ../..",
            "ls -l telegram-bot-api/bin/telegram-bot-api*"
            "13"
        ]
        count = 1
        for i in commands:
            try:
                result = subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				emit('message', { 'data': result.stdout.decode() })
				emit('message', { 'data': result.stderr.decode() })
                x = i.split()
                if count is 1:
                    import os
                    os.chdir("/opt/render/project/src")
                elif count is 3:
                    for s in x:
                        outputss = subprocess.run(["apt-get", "install", s, "-y"], capture_output=True).stdout.decode("utf-8")
                        emit("message", { "data": f"{s}\n{outputss}" }, broadcast=True)
                    count += 1
                    continue
                elif count is 5:
                    import os
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    os.chdir("telegram-bot-api/")
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    count += 1
                    continue
                elif count is 8:
                    import os
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    os.chdir("build/")
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    count += 1
                    continue
                elif count is 9:
                    import os
                    emit("message", { "data": "Starting compile!" })
                    os.system('CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang-10 CXX=/usr/bin/clang++-10 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..')
                    count += 1
                    continue
                elif count is 10:
                    import os
                    emit("message", { "data": "cmake" })
                    os.system("cmake --build . --target install")
                    count += 1
                    continue
                elif count is 11:
                    import os
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    os.chdir("/opt/render/project/src")
                    pwd = os.getcwd()
                    emit("message", { "data": pwd }, broadcast=True)
                    count += 1
                    continue
                elif count is 13:
                    import os
                    os.chdir("telegram-bot-api/bin/")
                    out = subprocess.run(["./telegram-bot-api", "--api-id=TELEGRAM_API_ID", "--api-hash=TELEGRAM_API_HASH"], capture_output=True).stdout.decode("utf-8")
                    emit("message", { "data": out })
                    count += 1
                    continue
                outputs = subprocess.run(x, capture_output=True).stdout.decode("utf-8")
                emit("message", { "data": f"{i}\n{outputs}" }, broadcast=True)
                count += 1
            except Exception as e:
                emit("message", { "data": f"Loop Error occured: {i}\n{e}" })
        emit("message", { "data": "Completed!" })
        import requests
        import os
        token = os.getenv("TOKEN")
        res = requests.get(f"http://127.0.0.1:8081/bot{token}/getMe").json()
        emit("message", { "data": res })
    except Exception as e:
        emit("message", { "data": f"Error occured: {e}" })

@socketio.on("message")
def message(message):
    List = ["Hello!", "Hi!", "Sasriya kaal!", "Jai hind!"]
    for i in List:
        emit("message", {"data": i}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
