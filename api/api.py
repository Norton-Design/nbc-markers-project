from flask import Flask
import time

app = Flask(__name__)

@app.route('/hello_world ')
def hello_world():
    return {'time': round(time.time(), 2)}