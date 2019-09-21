from flask import Blueprint, render_template,request,redirect,url_for,send_file,send_from_directory,current_app
from werkzeug import secure_filename
import uuid
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
import re
from .dbLayer import connectDB

searchDetails = Blueprint('searchDetails', __name__)

#client = MongoClient("mongodb+srv://recruiter:recruiter123@hackathon-ha58p.gcp.mongodb.net/hackathon?retryWrites=true&w=majority") #host uri
db = connectDB("recruiter","recruiter123")
#db = client.hackathon #Select the database
candidates_list = db.candidates_list #Select the collection name

@searchDetails.route("/search_list", methods=['POST'])
def search_list ():
    #Adding a Task
    search = request.values.get("searchname")
    name = candidates_list.find({"name": { '$regex' : search }})
    return render_template('searchlist.html',todos=name,flag=True)

@searchDetails.route("/searchlist")
def search ():
    return render_template('searchlist.html',todos="",flag=False)

@searchDetails.route('/resume/<filename>', methods=['GET', 'POST'])
def download(filename):    
    path = searchDetails.root_path
    path = path[0:len(path)-14]
    return send_from_directory(os.path.join(path,"resume"), filename, as_attachment=True)
