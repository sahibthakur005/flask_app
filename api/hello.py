from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World sahib ji"
@app.route("/upload")
def hello_upload():
    return "Hello upload"
