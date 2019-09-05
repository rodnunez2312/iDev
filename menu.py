from flask import Flask

app = Flask(__name__)

#Using routing we will create the multiple websites of our app
#all webpages are added to python function (aka routing or mapping)
@app.route('/') #this line especifies the url on your website to a python function
def homepage():
    return 'This is the home page' #return value of a function

@app.route('/Submenu/Rod')
def rod_page():
    return '<h2>This is rods page, bitches</h2>'

@app.route('/Submenu/<user>')
def profile_user(user):
    return "<h2>Hello %s<h2>" % user

@app.route('/Submenu/<int:id>') #here we are specifying the data type as interger
def id_num(id):
    return "<h2>Su numero de ID es  %s<h2>" % id

if __name__ == "__main__": #this is a quick check to make sure we only start our app only when this file is called directly
    app.run(debug=1)  #this will start our app and run in debug

