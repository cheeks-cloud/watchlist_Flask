from app import app

import urllib.request,json

from .models import movie

#get the api-key
Movie = movie.Movie
api_key = app.config['MOVIE_API_KEY']



#we importflask app instance 
# the lib mdule to help create a connection with the api
# use the json to format json response to python dictonary

#get the movie base url
base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):
  get_movies_url = base_url.format(category,api_key)#to replace the curly brackets

  with urllib.request.urlopen(get_movies_url) as url:
    get_movies_data = url.read()
    get_movies_reponse = json.loads(get_movies_data) #conver response to python dictionary

    movie_results = None

    if get_movies_reponse['results']:
      movie_results_list = get_movies_reponse['results']
      movie_results  = process_results(movie_results_list)#take in a list of dictionary object and returns a movie list

  return movie_results


def process_results(movie_list):
  movie_results = []
  for movie_item in movie_list:
    id = movie_item.get('id')
    tittle = movie_item.get('original_title')
    overview = movie_item.get('overview')
    poster = movie_item.get('poster_path')
    vote_average = movie_item.get('vote_average')
    vote_count = movie_item.get('vote_count')

    if poster:
      movie_object = Movie(id,tittle,overview, poster,vote_average,vote_count)
      movie_results.append(movie_object)

  return movie_results    