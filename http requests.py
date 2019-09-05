#http methods : GET and POST

#GET method: is the traditional method
#POST method: will be used if user wants to submit forms and information constantly

from flask import Flask, request ##here we are adding request module

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Method used: %s" % request.method

@app.route("/post_get", methods=['GET', 'POST']) #this will allow us to use both methods
def post_get():
    if request.method == 'POST':
        return "You are using POST method"
    else:
        return "You are probably using GET, the standard method"

if __name__ == "__main__":
    app.debug = True
    app.run()
