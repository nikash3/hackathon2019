
from flask import Blueprint, render_template

indexView = Blueprint('index', __name__)


@indexView.route("/")
def action ():
    #Adding a Task
    return "This is where form to signup and search would go"
