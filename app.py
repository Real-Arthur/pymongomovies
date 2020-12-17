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



# test route
#### instances of users with Pulp Fiction in list
@app.route('/')
def index():
    cursor = movie.find({"movies.title": "Pulp Fiction"},{"username": 1.0, "_id": 0})
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    return json_data

# # Get all movies from database
# @app.route('/movies')
# def get_movies():
#     return database.get_movies()

# # Get all movies in user's collection by user Id from User_Movie table
# @app.route('/library/<userId>', methods=['GET'])
# def get_library(userId):
#     return database.get_library(userId)

# # Add movie to user's collection
# @app.route('/library/<userId>', methods=['POST'])
# def add_library(userId):
#     return database.add_library(userId)

# # Searches The Movie Database API for queried actor/actress
# # Data provided by api.py get_person
# @app.route('/api/person', methods=['GET', 'POST'])
# def get_person():
#     data = request.get_json()
#     print(data)
#     results = api.get_person(data['query'])
#     return results

# # Searches The Movie Database API for queried actor/actress
# # Data provided by api.py get_title
# @app.route('/api/title', methods=['GET', 'POST'])
# def get_title():
#     data = request.get_json()
#     print(data)
#     results = api.get_title(data)
#     return results

# # Searches The Movie Database API for the cast of a queried movie by movie id
# # Data provided by api.py get_cast
# @app.route('/api/cast', methods=['GET'])
# def get_cast():
#     data = request.json['query']
#     print(f'data {data}')
#     results = api.get_cast(data)
#     return results

# # Searches The Movie Database API for details about a selected movie
# # Data provided by api.py get_details
# @app.route('/api/details', methods=['GET'])
# def get_details():
#     data = request.json['query']
#     print(f'data {data}')
#     results = api.get_details(data)
#     return results

# # Searches The Movie Database API for filmography of selected person
# # Data provided by api.py get_filmography
# @app.route('/api/filmography', methods=['GET'])
# def get_filmography():
#     data = request.json['query']
#     print(f'data {data}')
#     results = api.get_filmography(data)
#     return results

# run server
if __name__ == '__main__':
    app.run(debug=True)
