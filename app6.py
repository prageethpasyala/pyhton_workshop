from flask import Flask, request, Response
import json

app = Flask(__name__)

# DATABASE

books = {
    "1": { 'name': 'stargate', 'release_date': '1994' },
    "2": { 'name': 'Sunshine', 'release_date': '2007' },
    "3": { 'name': 'The Holiday', 'release_date': '2006' }
}

@app.route("/")
def hello():
    return 'Hello World'

@app.route("/books")
def get_all_movies():
    return json.dumps(books)

## READ
@app.route('/book/<id>', methods=['GET'])
def get_movie(id):
    return json.dumps(movie_db[id])

if __name__ == "__main__":
    app.run(host='127.0.0.1')






# curl GET http://127.0.0.1:5000/movie/ | jq
curl -X POST http://127.0.0.1:5000/movie/add -d '{"movie" : {"name" : "Matrix", "release_date" : "1999"}}' -H 'Content-Type: application/json'
jq
