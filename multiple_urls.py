from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #here we take 2 urls and we map them to the same functions/return value
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run()