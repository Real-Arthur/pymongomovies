import json
import requests
import os
import settings
from flask import Flask, jsonify, request
# from decouple import config

# Searches The Movie Database API for queried actor/actress by name
def get_person(value):
    url = 'https://api.themoviedb.org/3/search/person'
    params = dict(
        api_key=settings.API_KEY,
        query=value,
        page=1
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    return jsonify(data['results'])

# Searches The Movie Database API for queried movie by title
def get_title(value):
    url = 'https://api.themoviedb.org/3/search/movie'
    params = dict(
            api_key=settings.API_KEY,
            query=value,
            page=1
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    return jsonify(data)

# Searches The Movie Database API for cast of queried movie by movie id
def get_cast(value):
    resp = requests.get(f'https://api.themoviedb.org/3/movie/{value}/credits?api_key={settings.API_KEY}')
    data = resp.json()
    return jsonify(data)

# Searches The Movie Database API for details about a queried movie by movie id
def get_details(value):
    resp = requests.get(f'https://api.themoviedb.org/3/movie/{value}?api_key={settings.API_KEY}')
    data = resp.json()
    return jsonify(data)

# Searches The Movie Database API for filmography of person by id
def get_filmography(value):
    resp = requests.get(f'https://api.themoviedb.org/3/person/{value}/movie_credits?api_key={settings.API_KEY}')
    data = resp.json()
    return jsonify(data)