from flask import Flask
from .models import db
from config import Config
from flask_migrate import Migrate

app= Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

migrate = Migrate(app,db)


from . import routes 