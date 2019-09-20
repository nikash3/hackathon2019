
from flask import Blueprint, render_template
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

dbLayer = Blueprint('dbLayer', __name__)

title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

client = MongoClient("mongodb+srv://admin:admin@hackathon-ha58p.gcp.mongodb.net/test?retryWrites=true&w=majority") #host uri
db = client.test #Select the database
todos = db.todo #Select the collection name


@dbLayer.route("/list")
def action ():
    #Adding a Task
    name = todos.find({"name":"Task2"})
    return render_template('searchlist.html',todos=name,t=title,h=heading)
