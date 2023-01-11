from flask import Flask

# 实例化了一个Flask类
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"