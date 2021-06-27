from flask import Flask
from flask import render_template
app = Flask(__name__)

app.cervena = 0
app.modra = 0

@app.route("/")
def index():
    soucet = app.cervena + app.modra
    return render_template('index.html', cervena=app.cervena, modra=app.modra, progress="width: "+ str(app.cervena+app.modra) + "%")

@app.route("/klikadlo")
def klikadlo():
    soucet = app.cervena + app.modra
    return render_template('klikadlo.html', cervena=app.cervena, modra=app.modra, progress="width: "+ str(app.cervena+app.modra) + "%")


@app.route("/cervena")
def addCervena():
    app.cervena += 1
    return "Cervena úspěšně +1"

@app.route("/modra")
def addModra():
    app.modra += 1
    return "Modra úspěšně +1"


@app.route("/czech")
def pozdrav():
    return "Ahoj světě!"
