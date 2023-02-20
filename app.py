from flask import Flask
# pip install flask installs the module called flask (modules always lowercase names)
# from flask module import class Flask (first letter of class capital)

# we need to create an app, app is simply an object of the class Flask, ptyhon is object oriented, we're importing a class and then creating an object of the class.
app = Flask(__name__)
# only thing needed to be added is __name__, everytime we create a flask app we hv to name it, typically inside any pyhon script we have variable __name__ defined, __name__ variable refers to how a partcular script was invoked. When we execute print(__name__) in a python file we get __main__.

# a flask app has been created, now we need to tell flask that when a certain url is requested; what should be returned ?


# we are first registering a route or path (route - simply a part of url after domain name)
@app.route("/")
#@ is decorator; used to provide advanced functionality in use of libraries; refer article https://realpython.com/primer-on-python-decorators/ (referenced in cs50) for clarity
# / means empty route; homepage
def say_greetings():
  return "Get started"


# when url / is accessed; execute function say_greetings() which simply outputs "Assalam-o-Alaikum"

if __name__ == "__main__":
  print(
    "I'm inside the if now"
  )  #this line was inserted to check execution of if statement execution.
  app.run(host='0.0.0.0', debug=True)

#progressed till 17:40, proceed onwards...
