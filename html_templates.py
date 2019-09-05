from flask import Flask, render_template
app = Flask(__name__)

@app.route("/profile/<user>")
def profile(user):
    return render_template("profile.html", user=user) #NEVER use html code here, link html files instead

if __name__ == "__main__":
    app.debug = True
    app.run()