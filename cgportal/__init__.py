# app.py or app/__init__.py
from flask import Flask
from .views.index import indexView
from .views.dbLayer import dbLayer
from .views.searchDetails import searchDetails

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(indexView)
app.register_blueprint(dbLayer)
app.register_blueprint(searchDetails)