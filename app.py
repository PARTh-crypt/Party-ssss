from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "PARTH'S KISAN SAATHI - Server Running"
