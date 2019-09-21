from flask import Blueprint, render_template,request,redirect,url_for
from werkzeug import secure_filename
import uuid
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

dbLayer = Blueprint('dbLayer', __name__)
#user = "admin"
#client = MongoClient("mongodb+srv://"+user+":"+user+"@hackathon-ha58p.gcp.mongodb.net/hackathon") #host uri
#client = MongoClient(url='mongodb+srv://@hackathon-ha58p.gcp.mongodb.net',username='admin',password='admin',authSource='hackathon',authMechanism='SCRAM-SHA-256')
#db = client.hackathon #Select the database
#candidates_list = db.candidates_list #Select the collection name

 #@dbLayer.route("/connect",methods=['POST'])
def connectDB (username,password):
    client = MongoClient("mongodb+srv://"+username+":"+password+"@hackathon-ha58p.gcp.mongodb.net/hackathon") #host uri
    db = client.hackathon
    return db
