from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/instructions")
def instructions():
    return render_template("instruction.html")

if __name__ == "__main__":
    app.run()
