from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/upload")
def hello_upload():
    return "Hello upload"
