from flask import Flask, request, Response
import json

app = Flask(__name__)

book_db = {
    "1": { 'name': 'Java dumps', 'release_date': '1994' },
    "2": { 'name': 'A Cloud Guru', 'release_date': '2007' },
    "3": { 'name': 'Lambda functions', 'release_date': '1995' },
    "4": { 'name': 'SQL for beginers', 'release_date': '2018' },
    "5": { 'name': 'CCNA dumps', 'release_date': '2007' },
    "6": { 'name': 'Web Develop', 'release_date': '2006' }
}


# home page---------------------
@app.route("/home")
def hello():
    return "Hello World"

# display list------------------
@app.route("/")
def moviesaaaa():
    
    html_response = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                    table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                    }

                    td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                    }

                    tr:nth-child(even) {
                    background-color: #dddddd;
                    }
                    </style>
                    </head>
                    <body>

                    <h2>Book Library</h2>

                    <table>
                    <tr>
                        <th>Name</th>
                        <th>Release Date</th>
                        
                    </tr>
                    """
    for m in book_db:
        html_response += "<ul><tr><td>"+ "<a href='/book/" + m + "'>" + book_db[m]['name'] + "</a>" + "</td><td>"+ book_db[m]['release_date'] +"</td></tr></ul>"
    
    html_response += "</table></body></html>"
                                                 
    return html_response
   
# find book-----------------------------
@app.route("/book/<book_id>")

def get_book(book_id):
    html_response = "<ul>"
    # return json.dumps(book_db[book_id])
    html_response += "<a href='/'> Go Back  </a>  " + json.dumps(book_db[book_id])
    return html_response



# add a book --------------------------
@app.route("/book/add", methods=['POST'])
def add_book():
    index = len(book_db) + 1
    req_data = request.get_json()
    book = req_data['book']      #{"book": { "name": "jupitoer dummiesw","release_date": "May 1922"}

    new_book = { str(index) : book }
    book_db.update(new_book)
    return "Book added sucessfully!!"



# # delete a book --------------------------
# @app.route("/book/del", methods=['POST'])
# def add_book():
    
    









if __name__ == "__main__":
    app.run(host='127.0.0.1')