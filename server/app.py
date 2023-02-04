from flask import Flask



app = Flask(__name__)  # notice that the app instance is called `app`, this is very important.


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"