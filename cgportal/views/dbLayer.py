from flask import Blueprint, render_template,request,redirect,url_for
from werkzeug import secure_filename
import uuid
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
from .resumeParser import parser
import os

dbLayer = Blueprint('dbLayer', __name__)

title = "TODO sample application with Flask and MongoDB"
heading = "TODO Reminder with Flask and MongoDB"

client = MongoClient("mongodb+srv://admin:admin@hackathon-ha58p.gcp.mongodb.net/hackathon?retryWrites=true&w=majority") #host uri
db = client.hackathon #Select the database
candidates_list = db.candidates_list #Select the collection name
    
@dbLayer.route("/submit", methods=['POST'])
def submit ():
    f = request.files['file']
    fnameOrg = secure_filename(f.filename)
    fnameId = secure_filename(str(uuid.uuid4()))
    fname = fnameId + fnameOrg
    f.save(os.path.join("resume", fname))
    data = parser(os.path.join("resume", fname))
    #Adding a Task
    email=request.values.get("email")
    name=request.values.get("name")

    candidates_list.insert({ "email": email, "name":name, "file": fname, "skills": data["skills"], "contact_number": data["mobile_number"], "experience": data["total_experience"]})
    return redirect("/searchlist")
