""" using replit's own database in your application: https://replit-py.readthedocs.io/en/latest/
https://docs.replit.com/hosting/databases/replit-database#:~:text=Using%20Replit%20Database%E2%80%8B&text=This%20database%20can%20be%20accessed,pairs%20of%20a%20Python%20dictionary. """

# NOTE: don't call application flask.py (it will conflict with flask itself - as per flask documentation)

from flask import Flask, request, render_template, jsonify
from cs50 import SQL
#pip install cs50 used in shell to install cs50 library
# pip install flask installs the module called flask (modules always lowercase names)
# from flask module import class Flask (first letter of class capital)
# jsonify is a helper function that converts any given data to json

# we need to create an app, app is simply an object of the class Flask, ptyhon is object oriented, we're importing a class and then creating an object of the class.
app = Flask(__name__)

# 1 app is an instance of the class Flask - it is our wsgi application (web-server-gateway-interface), its first argument is the name of the application's module or package (__name__ is a convenient shortcut for this, it refers to the current app, this is needed so flask knows where to look for resources such as templates & static files).

# 2 everytime we create a flask app we hv to name it, typically inside any pyhon script we have variable __name__ defined, __name__ variable refers to how a partcular script was invoked. if it was invoked using python app.py; the name variable is going to have the value __main__.

# a flask app has been created, now we need to tell flask that when a certain url is requested; what should be returned ?

db = SQL("sqlite:///sample.db")  #creating the database

#creating a python list for displaying data to webpage
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Karachi',
  'salary': 'Rs. 100,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Lahore',
  'salary': 'Rs. 200,000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Faisalabad',
}]

#creating a list of interests for serving to webpage
INTERESTS = ['Coding', 'Fishing', 'Reading', 'Partying']

#creating empty dictionary to store members data
MEMBERS = {}


# we are first registering a route or path (route - simply a part of url after domain name)
@app.route("/")
#@ is decorator; used to provide advanced functionality in use of libraries; refer article https://realpython.com/primer-on-python-decorators/ (referenced in cs50) for clarity
# / means empty route; homepage
# here the route() decorator used to tell flask what URL should trigger our function, this function returns the message we want to display in the user's browser (default content type is html)
def say_greetings():
  #return "Assalam-O-Alaikum"
  #above line commented out after implementing render_template function
  return render_template("home.html", jobs=JOBS)


# when url / is accessed; execute function say_greetings() which simply outputs "Assalam-o-Alaikum"


@app.route("/api/jobs")
# /api/route added in address to identify that instead of html some api data will be returned when this url is accessed.
def list_jobs():
  return jsonify(JOBS)  # jsonify renders/returns the JOBS list as json data


@app.route("/login", methods=["GET", "POST"])
def login():

  if request.method == "POST":
    name = request.form.get("firstname")
    birthdate = request.form.get("birthdate")
    interest = request.form.get("interests")
    if not name or not birthdate or interest not in INTERESTS:
      return "Form data not entered correctly/completely ! Please re-submit."
    db.execute(
      "INSERT INTO members (name, birthdate, interest) VALUES (?, ?, ?)", name,
      birthdate, interest)
    members = db.execute("SELECT * FROM ")
    return render_template("registered.html", name=name)
  return render_template("login.html", interests=INTERESTS)


if __name__ == "__main__":
  print(
    "I'm inside the if now"
  )  #this line was inserted to check execution of if statement execution.
  app.run(host='0.0.0.0', debug=True)

# onwards only important notes regarding the jovian careers video:
# 1. bootstrap navbar example download, the examples page online corresponds to the serial wise examples downloaded, navbar shadow implemented.
# 2. mailto links serached in google, they are used for mailing with predefined subject, recipient etc. construct custom mailto url link at mailtolink.me
# 3. a target="_blank" opens a new tab
# 4. create a new repository in github, no readme/no gitignore/no license. (this allows to import code from another repository), click import code and paste other repository code into it. it pulls all code from another repository.
