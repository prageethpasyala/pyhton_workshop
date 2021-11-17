from flask import Flask, request, Response, jsonify 
import json

app = Flask(__name__)

book_db = {
    "1": { 'name': 'Python for dummies', 'author': 'Sam', 'serial': '513120'},
    "2": { 'name': 'Linux for dummies', 'author': 'Kai', 'serial': '7617930'},
    "3": { 'name': 'PHP for dummies', 'author': 'Jim', 'serial': '1010408'}
}

# find the last index
def _find_next_id():
    return max(book["id"] for book in book_db) + 1


@app.route("/")
def hello():
    html_response = "<ul>"
    for m in book_db:
        html_response += "<li>" + "<a href='/book/" + m + "'>" + book_db[m]["name"] + "</a>" + "</li>"
    html_response += "</ul>"
    return html_response 


# READ
@app.route("/book/<book_id>")
def get_movie(book_id):
    return json.dumps(book_db[book_id])



# CREATE    - POST
@app.route("/book/add", methods=['POST'])
def add_book():
    req_data = request.get_json()
    book = req_data['book']       # { name: "something", release_date: "something" }
    book["id"] = _find_next_id()
    new_book = { "5" : book }
    book_db.update(new_book)
    return "The new book was added successfully"

# def update_book():
#     if request.is_json:
#         book = request.get_json()
#         book["id"] = _find_next_id()
#         # books.append(book)
#         books.update({"author": "Sam"})
#         return book, 201
#     return {"error": "Request must be JSON"}, 415    



if __name__ == "__main__":
    app.run(host='127.0.0.1')

# curl -X POST http://127.0.0.1:5000/book/add -d '{"book" : {"name" : "Go for dummies", "author":"BNB", "serial" : "1999"}}' -H 'Content-Type: application/json'
# curl -X GET http://127.0.0.1:5000/movie/2