import unittest
from models import movie


Movie = movie.Movie

class MovieTest(unittest.TestCase):
  
  def setUp(self):
    self.new_movie = Movie(1234,'Python must be sorcery','a thrilling series',
    'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

  # def test __init(self):
  #   self.assertTrue(self.new_movie.tittle,"1234")
  #   self.assertTrue(self.new_movie.overview,"Python must be sorcery")
  #   self.assertTrue(self.new_movie.poster,"a thrilling series")
  #   self.assertTrue(self.new_movie.tittle,"1234")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie,Movie))







if __name__ == '__main__':
  unittest.main()