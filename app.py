from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")