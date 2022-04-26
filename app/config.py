class Config:
  pass #gen parent class

class ProdConfig(Config):
  pass #production configuration class

class DevConfig(Config):
  DEBUG = True
