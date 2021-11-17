from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config
import json

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)
class Movies(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_date = db.Column(db.Integer)


# movie_db = {
#     "1": { 'name': 'Stargate', 'release_date': '1994' },
#     "2": { 'name': 'Sunshine', 'release_date': '2007' },
#     "3": { 'name': 'The Holiday', 'release_date': '2006' }
# }

@app.route("/")
def hello():
    return "Hello World"

@app.route("/movies")
def movies():
    #Retriving all the movies 
    movies = Movies.query.all()


    html_response = "<ul>"
    for m in movies:
        html_response += "<li>" + "<a href='/movie/" + m.id + "'>" + m.name + "</a>" + "</li>"
    html_response += "</ul>"
    return html_response


# READ
@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    
    return json.dumps(movie_db[movie_id])

# CREATE    - POST
@app.route("/movie/add", methods=['POST'])
def add_movie():
    req_data = request.get_json()
    movie = req_data['movie']       # { name: "something", release_date: "something" }

    new_movie = { "2" : movie }
    movie_db.update(new_movie)
    return "Movie was added successfully"

if __name__ == "__main__":
    app.run(host='127.0.0.1')




### new movie
# { "movie" : { "name" : "The Matrix", "release_date" : "1999"} }






# READ      - GET
# UPDATE    - PUT
# DELETE    - GET