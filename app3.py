
from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "name": "Python for dummies", "author": "Sam", "serial": 513120},
    {"id": 2, "name": "Linux for dummies", "author": "Kai", "serial": 7617930},
    {"id": 3, "name": "PHP for dummies", "author": "Jim", "serial": 1010408},
]

def _find_next_id():
    return max(book["id"] for book in books) + 1

@app.get("/books")
def get_books():
    return jsonify(books)

@app.post("/books")
def add_book():
    if request.is_json:
        book = request.get_json()
        book["id"] = _find_next_id()
        books.append(book)
        return book, 201
    return {"error": "Request must be JSON"}, 415


@app.put("/books")
def update_book():
    if request.is_json:
        book = request.get_json()
        book["id"] = _find_next_id()
        # books.append(book)
        books.update({"author": "Sam"})
        return book, 201
    return {"error": "Request must be JSON"}, 415    

if __name__ == '__main__':
   app.run(debug = True)



# POST
# curl -i http://127.0.0.1:5000/books \
# -X POST \
# -H 'Content-Type: application/json' \
# -d '{"name":"Java for dummies", "author": "Berlin", "serial": 357022}'

# GET
# curl -i http://127.0.0.1:5000/books