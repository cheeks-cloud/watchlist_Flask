class Config:
   #gen parent class
   MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={} "
                           
#   now_showing_movie
class ProdConfig(Config):
    pass #production configuration class

class DevConfig(Config):
    DEBUG = True
