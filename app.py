from flask import Flask
from flask import render_template
app = Flask(__name__)

app.r = 0
app.g = 0
app.b = 0
app.y = 0
INCREMENT=1
MAXIMUM=100

@app.route("/")
def index():
    return render_template('index.html', r=app.r, b=app.b, g=app.g, y=app.y, maximum=MAXIMUM)

@app.route("/klikadlo")
def klikadlo():
    return render_template('klikadlo.html', progress="width: "+ str(app.r+app.b+app.g+app.y) + "%", maximum=MAXIMUM)

# Pridavani prichozich hodnot
@app.route("/r")
def addR():
    app.r += INCREMENT
    return True

@app.route("/b")
def addM():
    app.b += INCREMENT
    return True

@app.route("/g")
def addG():
    app.g += INCREMENT
    return True

@app.route("/y")
def addY():
    app.y += INCREMENT
    return True



@app.route("/czech")
def pozdrav():
    return "Ahoj světě!"
