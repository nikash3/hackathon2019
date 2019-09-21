from flask import Blueprint, render_template,request,redirect,url_for
from werkzeug import secure_filename
from .dbLayer import connectDB
from .resumeParser import parser
import uuid
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os


candidateSubmit = Blueprint('candidateSubmit', __name__)

@candidateSubmit.route("/submit", methods=['POST','GET'])
def submit ():
    db = connectDB("admin","admin") #connect to DB
    #db = client.hackathon
    email=request.values.get("email")
    name=request.values.get("name")
    candidates_lists = db.candidates_list
    f = request.files['file']
    fnameOrg = secure_filename(f.filename)
    fnameId = secure_filename(str(uuid.uuid4()))
    fname = fnameId + fnameOrg
    f.save(os.path.join("resume", fname))
    data = parser(os.path.join("resume", fname))
    #Adding a Task
    email=request.values.get("email")
    name=request.values.get("name")

    candidates_lists.insert({ "email": email, "name":name, "file": fname, "skills": data["skills"], "contact_number": data["mobile_number"], "experience": data["total_experience"]})
    return redirect("/searchlist")
