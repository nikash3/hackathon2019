
from flask import Blueprint, render_template
from .elasticSearch import createIndex

indexView = Blueprint('index', __name__)


@indexView.route("/")
def action ():
    #Adding a Task
    createIndex()
    return render_template('index.html')
