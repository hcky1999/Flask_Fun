from flask import Flask, render_template, request
app = Flask(__name__)    

#flask_Fundamentals                         
#Assignment: Understanding Routing

@app.route("/")
def hello_world():
    return '<h1>Hello World</h1>'


@app.route('/Dojo')
def dojo():
  return "<h3>Dojo</h3>"

@app.route('/say/flask')
def flask():
    return "Hi Flask"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name' 
def hello(name):        # type Michael and John
    print(name)
    return "Hi "+ name

@app.route('/repeat/35/<name>')
def str35_hello (name):
    print (name)
    return  name*int("35")

@app.route('/repeat/99/<name>')
def str99dogs (name):
    print (name)
    return name*int("99")


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
