from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello Jacch"

@app.route("/test")
def test():
    return "just a test"

if __name__=="main":
    app.run()