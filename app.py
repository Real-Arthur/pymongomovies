from flask import Flask, request, jsonify, json
from peewee import *
from marshmallow import Schema, fields
import database
import settings
import api
import pymongo
from bson.json_util import dumps, loads

app = Flask(__name__)

client = pymongo.MongoClient(f"mongodb+srv://Real_Arthur:{settings.DB_PASSWORD}@practice.cwduj.mongodb.net/movies?retryWrites=true&w=majority")
db = client.movies
movie = db.movie


@app.route('/')
def index():
    return 'Go for pymongomovies'

# Create new user
@app.route('/db/users', methods=['POST'])
def add_user():
    username = request.json['username']
    password = request.json['password']
    cursor = movie.insert_one(
        {
            "username": username,
            "password": password,
            "movies": []
        }
    )
    return '200'

# Add new movie to user's movie array
@app.route('/db/users/<string:username>', methods=['PUT'])
def add_movie(username):
    id = request.json['id']
    title = request.json['title']
    overview = request.json['overview']
    release_date = request.json['release_date']
    poster_path = request.json['poster_path']
    cursor = movie.update_one(
        {
            "username": username
        },
        {
            "$push":
            { "movies":
                {
                    "id" : id,
                    "title" : title, 
                    "overview" : overview, 
                    "release_date" : release_date, 
                    "poster_path" : poster_path
                }
            }
        }
    )
    return '200'

# test route
#### instances of users with Pulp Fiction in movie list
@app.route('/db/common')
def get_one_in_all():
    movie_to_find = request.json['query']
    cursor = movie.find({"movies.title": movie_to_find},{"username": 1.0, "_id": 0})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

# Gets movie list and username from every user
@app.route('/db/users', methods=['GET'])
def get_all():
    cursor = movie.find({}, { "username" : 1.0, "movies" : 1.0, "_id": 0.0 })
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

# Gets movie list by username
@app.route('/db/users/<string:username>', methods=['GET'])
def get_library(username):
    cursor = movie.find({ "username" : username }, { "movies" : 1.0, "_id" : 0.0 })
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

# Searches The Movie Database API for queried actor/actress
# Data provided by api.py get_person
@app.route('/api/person', methods=['GET', 'POST'])
def get_person():
    data = request.get_json()
    print(data)
    results = api.get_person(data['query'])
    return results
    
# Searches The Movie Database API for queried actor/actress
# Data provided by api.py get_title
@app.route('/api/title', methods=['GET', 'POST'])
def get_title():
    data = request.get_json()
    print(data)
    results = api.get_title(data['query'])
    return results

# Searches The Movie Database API for the cast of a queried movie by movie id
# Data provided by api.py get_cast
@app.route('/api/cast', methods=['GET'])
def get_cast():
    data = request.json['query']
    print(f'data {data}')
    results = api.get_cast(data)
    return results

# Searches The Movie Database API for details about a selected movie by movie id
# Data provided by api.py get_details
@app.route('/api/details', methods=['GET'])
def get_details():
    data = request.json['query']
    print(f'data {data}')
    results = api.get_details(data)
    return results

# Searches The Movie Database API for filmography of selected person
# Data provided by api.py get_filmography
@app.route('/api/filmography', methods=['GET'])
def get_filmography():
    data = request.json['query']
    print(f'data {data}')
    results = api.get_filmography(data)
    return results

# run server
if __name__ == '__main__':
    app.run(debug=True)
