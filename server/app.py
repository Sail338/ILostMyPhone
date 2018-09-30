from flask import Flask,request
from funk import three_circle

app = Flask(__name__)

@app.route('/read_points')
def read_points():
    print(request)
    return "done"
