import os
import json
from flask import Flask, render_template
# This is how you would import the Flask class from the flask module.
# Render_template is a function that allows you to render html files.


app = Flask(__name__)
# This is how you would create an instance of the Flask class.


@app.route('/')
def index():
    return render_template('index.html')
# This is how you would get python to be able to run the html file.
# This is a little like javascript DOM manipulation, but in python.


@app.route('/about')
def about():
    data = []
# The data variable is used to store the data from the json file.
    with open('data/mock_data.json', 'r') as json_data:
# This is how you would open a json file in python. r is for read.
        data = json.load(json_data)
# This is how you would load the data from the json file.
    return render_template('about.html', page_title="About", mock_data=data)
# data=data is how you would pass the data from the json file to the html file.
# This is how you would create a route for the about page.
# You would then repeat this for every page you wish to create.
# This is the basic structure of a flask app.

@app.route('/about/<member_name>')
def about_member(member_name):
# This is how you would create a route for a specific member.
    member = {}
# member is an empty dictionary.
    with open('data/mock_data.json', 'r') as json_data:
# This is how you would open a json file in python. r is for read.
        data = json.load(json_data)
# This is how you would load the data from the json file as a list of dictionaries.
        for obj in data:
# This is how you would loop through the list of dictionaries.
            if obj['url'] == member_name:
# This is how you would check if the url key pair in the json file is the same as the member_name.
                member = obj
# member is now the dictionary that has the same url key pair as the member_name.
    return render_template('member.html', member=member)
# This is how you would pass the member dictionary to the html file.
# This first 'member' is the variable name being passed through into our html file.
# The second 'member' is the member object we created above on line 24.


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact")
# This is how you would create a route for the contact page.


@app.route('/careers')
def careers():
    return render_template('careers.html', page_title="Careers")
# Having a template makes it easier to change things that would require a change to every page
# as you would only need to change the template and it would change on every page. Copying the template


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True )
# This is how you would run the app.
# This code defines the host and port that the app will run on.
# And it also sets the debug to true, so that you can see the errors in the terminal.
# Always remember to set the debug to false when you are done with the app.
# This always runs first.