
# from .views import app
from flask import Flask
from .config import DevConfig

#INITIALIZING THE APPLICATION
app = Flask(__name__)


#setup the configuration 
#import devconfig to ensure our applicaion uses the new configurations then pass it in app.config
#we then remove debug from run since devconfig is debuging
app.config.from_object(DevConfig)


from app import views




