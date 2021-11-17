from flask import Flask, redirect, url_for

#from my_python_app.main import book
app = Flask(__name__)
  

mybooks = {
  1 : {
    "name" : "Java for dummies",
    "year" : 2004,
    "author" : "Elvi"
  },
  2 : {
    "name" : "Python for dummies",
    "year" : 2007,
    "author" : "Jeebrial"
  },
  "child3" : {
    "name" : "Linux for dummies",
    "year" : 2011,
    "author" : "Pascal"
  }
}

@app.route("/")
def hello():
    return "<h1>hello world</h1><button>sub</button>"



@app.route('/admin')  #decorator for route(argument) function
def hello_admin():     #binding to hello_admin call
   return 'Hello Admin'    
  
@app.route('/guest/<guest>')
def hello_guest(guest):    #binding to hello_guest call
   return 'Hello %s as Guest' % guest
  
@app.route('/user/<name>')
def hello_user(name):    
   if name =='admin':  #dynamic binding of URL to function
      return redirect(url_for('hello_admin'))  
   else:
      return redirect(url_for('hello_guest', guest = name))
  
if __name__ == '__main__':
   app.run(debug = True)