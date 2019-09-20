
from flask import Blueprint, render_template

indexView = Blueprint('index', __name__)


@indexView.route("/")
def action ():
    #Adding a Task
    return render_template('index.html')
