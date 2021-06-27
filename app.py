from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/czech")
def pozdrav():
    return "Ahoj světě!"
