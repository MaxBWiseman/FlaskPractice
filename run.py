import os
from flask import Flask, render_template
#This is how you would import the Flask class from the flask module.
#Render_template is a function that allows you to render html files.


app = Flask(__name__)
#This is how you would create an instance of the Flask class.


@app.route('/')
def index():
    return render_template('index.html')
#This is how you would get python to be able to run the html file.
#This is a little like javascript DOM manipulation, but in python.


@app.route('/about')
def about():
    return render_template('about.html')
#You would then repeat this for every page you wish to create.
#This is the basic structure of a flask app.


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/careers')
def careers():
    return render_template('careers.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True )
#This is how you would run the app.
#This code defines the host and port that the app will run on.
#And it also sets the debug to true, so that you can see the errors in the terminal.
#Always remember to set the debug to false when you are done with the app.
#This always runs first.