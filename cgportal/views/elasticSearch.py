from flask import Blueprint, render_template,request,redirect,url_for,send_file,send_from_directory,current_app
from werkzeug import secure_filename
import uuid
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
from elasticsearch import Elasticsearch

elasticSearch = Blueprint('elasticSearch', __name__)
client = MongoClient("mongodb+srv://recruiter:recruiter123@hackathon-ha58p.gcp.mongodb.net/hackathon?retryWrites=true&w=majority") #host uri
db = client.hackathon #Select the database
candidates_list = db.candidates_list #Select the collection name

@elasticSearch.route("/search")
def search ():
    HOST_URLS = ["http://127.0.0.1:9200"]
    es_conn = Elasticsearch(HOST_URLS)
    INDEX_NAME = "myproject"
    TYPE_NAME_USER = "user"
    res = es_conn.indices.create(index= INDEX_NAME, ignore=400)
    search = request.values.get("search")
    return "Cluster Name: " + es_conn.cluster.state(metric=["cluster_name"])['cluster_name']

@elasticSearch.route("/elastic_search", methods=['POST'])
def elasticsearch ():
    search = request.values.get("searchname")
    name = request.values.get("name")
    email = request.values.get("email")
    contact_no = request.values.get("contact_no")
    skills = request.values.get("skills")
    experience = request.values.get("experience")
    # 'on' if checked else 'None' 
    return render_template('elasticsearch.html',todos=name,flag=True)

@elasticSearch.route("/elasticsearch")
def elastic ():
    return render_template('elasticsearch.html',todos="",flag=False)