from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app)#, logger=True, engineio_logger=True)

@app.route("/")
def index():
  return render_template('index.html')

@socketio.on('connect')
def test_connect():
  emit('message', { 'data': "Connected" })

@socketio.on("check")
def check(message):
  try:
    import requests
    import os
    token = os.getenv("TOKEN")
    res = requests.get(f"http://localhost:8081/bot{token}/getMe")
    emit("message", { "data": res.text })
  except Exception as e:
    emit("message", { "data": f"Error occured: {e}" })

@socketio.on("start")
def start(message):
  import os
  pwd = os.getcwd()
  emit("message", { "data": pwd })
  os.chdir("/opt/render/project/src")
  pwd = os.getcwd()
  emit("message", { "data": pwd })
  import subprocess
  output = subprocess.run("docker run -d -p 8081:8081 --name=telegram-bot-api --restart=always -v telegram-bot-api-data:/var/lib/telegram-bot-api -e TELEGRAM_API_ID=27269597 -e TELEGRAM_API_HASH=ef91ab7dfb77baea3d5f87e5d6cd5744 aiogram/telegram-bot-api:latest", capture_output=True)
  emit("message", { "data": f"Docker: {output}" })
  output = subprocess.run("ls -alh", capture_output=True)
  emit("message", { "data": f"ls: {output}" })

@socketio.on("message")
def message(message):
  List = ["Hello!", "Hi!", "Sasriya kaal!", "Jai hind!"]
  for i in List:
    emit("message", { "data": i }, broadcast=True)

if __name__ == "__main__":
  socketio.run(app)
