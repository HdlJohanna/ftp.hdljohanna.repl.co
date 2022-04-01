from flask import Flask, send_from_directory, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://github.com/HdlJohanna/")

@app.route("/<rname>/<filename>")
def send(rname,filename):
  return send_from_directory(rname,filename)

app.run("0.0.0.0",8080)
