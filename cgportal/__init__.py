# app.py or app/__init__.py
from flask import Flask
from .views.index import indexView
from .views.dbLayer import dbLayer
from .views.searchDetails import searchDetails
from .views.candidateSubmit import candidateSubmit
from .views.resumeParser import resumeParser
from .views.elasticSearch import elasticSearch

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(indexView)
app.register_blueprint(dbLayer)
app.register_blueprint(searchDetails)
app.register_blueprint(candidateSubmit)
app.register_blueprint(resumeParser)
app.register_blueprint(elasticSearch)

