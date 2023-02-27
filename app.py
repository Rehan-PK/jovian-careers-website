# NOTE: don't call application flask.py (it will conflict with flask itself - as per flask documentation)

from flask import Flask, render_template
# pip install flask installs the module called flask (modules always lowercase names)
# from flask module import class Flask (first letter of class capital)

# we need to create an app, app is simply an object of the class Flask, ptyhon is object oriented, we're importing a class and then creating an object of the class.
app = Flask(__name__)

# 1 app is an instance of the class Flask - it is our wsgi application (web-server-gateway-interface), its first argument is the name of the application's module or package (__name__ is a convenient shortcut for this, it refers to the current app, this is needed so flask knows where to look for resources such as templates & static files).

# 2 everytime we create a flask app we hv to name it, typically inside any pyhon script we have variable __name__ defined, __name__ variable refers to how a partcular script was invoked. if it was invoked using python app.py; the name variable is going to have the value __main__.

# a flask app has been created, now we need to tell flask that when a certain url is requested; what should be returned ?

# we are first registering a route or path (route - simply a part of url after domain name)
@app.route("/")

#@ is decorator; used to provide advanced functionality in use of libraries; refer article https://realpython.com/primer-on-python-decorators/ (referenced in cs50) for clarity
# / means empty route; homepage
# here the route() decorator used to tell flask what URL should trigger our function, this function returns the message we want to display in the user's browser (default content type is html)
def say_greetings():
  #return "Assalam-O-Alaikum"
  #above line commented out after implementing render_template function
  return render_template("home.html")

# when url / is accessed; execute function say_greetings() which simply outputs "Assalam-o-Alaikum"

if __name__ == "__main__":
  print(
    "I'm inside the if now"
  )  #this line was inserted to check execution of if statement execution.
  app.run(host='0.0.0.0', debug=True)

#progressed till 17:40, proceed onwards...
