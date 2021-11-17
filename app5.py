# allow both GET and POST requests
from flask import Flask, request, jsonify

app = Flask(__name__)

books = {
    "1": { 'name': 'Python for dummies', 'author': 'Sam', 'serial': '513120'},
    "2": { 'name': 'Linux for dummies', 'author': 'Kai', 'serial': '7617930'},
    "3": { 'name': 'PHP for dummies', 'author': 'Jim', 'serial': '1010408'}
}

def _find_next_id():
    return max(book["id"] for book in books) + 1

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        author = request.form.get('author')
        
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(author)
                  

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Name: <input type="text" name="name"></label></div>
               <div><label>author: <input type="text" name="author"></label></div>
               <div><label>serial: <input type="text" name="serial"></label></div>
               <input type="submit" value="Submit">
           </form>'''


@app.route("/books/<id>")
def get_book(book_id):
    return books[book_id]




if __name__ == '__main__':
   app.run(debug = True)