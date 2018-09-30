from flask import Flask,request

app = Flask(__name__)

@app.route('/read_points')
def read_points():
    print(request)
    return "done"
