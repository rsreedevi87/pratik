from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_flask():
    return "This is my first flask program"



@app.route("/second")
def second_flask():
    return "Python function"

app.run()
