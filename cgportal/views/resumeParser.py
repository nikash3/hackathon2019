from flask import Blueprint, render_template
from pyresparser import ResumeParser
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

resumeParser = Blueprint('resumeParser', __name__)

title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

client = MongoClient("mongodb+srv://admin:admin@hackathon-ha58p.gcp.mongodb.net/test?retryWrites=true&w=majority") #host uri
db = client.test #Select the database
todos = db.todo #Select the collection name

@resumeParser.route("/resume")
def action ():
    data = ResumeParser('C:/Users/gupta/Downloads/SHIVANSHU_GUPTA.pdf').get_extracted_data()
    insertedData = todos.insert({"skills": data["skills"], "email": data["email"], "contact_number": data["mobile_number"], "experience": data["total_experience"]})
    return render_template('searchlist.html',todos=insertedData,t=title,h=heading)
