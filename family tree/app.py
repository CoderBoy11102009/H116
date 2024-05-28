# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Atish" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)
@app.route("/father")
def home1():
# define the route to father webpage
    name = "Sunil" # write your name
    age = "45" # write your age

    return render_template('father.html' , name = name , age = age)
@app.route("/mother")
def home2():
# define the route to the mother webpage
    name = "Vimi"
    age = "40"

    return render_template('mother.html', name = name, age = age)
@app.route("/friend")
def home3():
# define the route to the friends webpage
    name = "Edward"
    age = "14"

    return render_template('friend.html', name = name, age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
