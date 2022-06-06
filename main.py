from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html")
    
@app.route("/form")
def form():
    return render_template("form.html")