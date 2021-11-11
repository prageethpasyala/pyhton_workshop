import _json
from flask import Flask, request , Response



app = Flask(__name__)

book_db = {
    "1" : {'name' : 'Dummies for Python', 'author' : 'Sam'},
    "2" : {'name' : 'Dummies for JAVA', 'author' : 'Danny'}
}

@app.route("/")
def hello():
    return "hello world"

@app.route("/books")
def world():
    return book_db

#read
@app.route("/books/<id>")
def get_movie(book_id):
    return book_db[book_id]


if __name__=="__main__":
    app.run(host='127.0.0.1')

    