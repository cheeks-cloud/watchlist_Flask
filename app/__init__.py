
from flask import Flask
from .config import DevConfig

#INITIALIZING THE APPLICATION
app = Flask(__name__,instance_relative_config = True)


#setup the configuration 
#import devconfig to ensure our applicaion uses the new configurations then pass it in app.config
#we then remove debug from run since devconfig is debuging
#app.config connects to the config.py and append its contents to app.config

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views




