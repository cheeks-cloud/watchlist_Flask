#view root page that returns inde aas its data
#the rendr template function is from flaskwhenits run we want it to import index
from flask import render_template
from app import app
from .request import get_movies


@app.route('/')
def index():
  # return render_template('index.html')

  # message = 'Hello world!'
  # return render_template('index.html', message = message)

  title = 'Home - WELCOME tO movie review'

  popular_movies = get_movies('popular')
  upcoming_movie = get_movies('upcoming')
  now_showing_movie = get_movies('now_playing')
  
  return render_template('index.html', title = title,
  popular = popular_movies, upcoming = upcoming_movie, now_playing =
  now_showing_movie)

#id from the template,movie_id from view
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  return render_template('movie.html',id = movie_id)




  