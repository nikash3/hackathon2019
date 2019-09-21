from flask import Blueprint, render_template,request,redirect,url_for,send_file,send_from_directory
from .dbLayer import connectDB
from array import *
from elasticsearch import Elasticsearch


elasticSearch = Blueprint('elasticSearch', __name__)
db = connectDB("recruiter","recruiter123")
candidates_list = db.candidates_list #Select the collection name
es = Elasticsearch()

def createIndex ():
    es.indices.delete(index='student', ignore=[400, 404])
    todos = candidates_list.find()
    for todo in todos :
        insertToIndex(todo)

def insertToIndex (record):
    stu_record = { "name": record["name"], "file": record["file"], "email": record["email"], "skills": record["skills"] , "contact_number" : record["contact_number"], "experience": record["experience"]}
    es.index(index="student", doc_type="student-resume", id=record["_id"],body=stu_record)

@elasticSearch.route("/elastic_search", methods=['POST'])
def elasticsearch ():
    fields = []
    search = request.values.get("searchname")
    varall = request.values.get("all")
    
    name = request.values.get("name")
    if name == 'on' or varall == 'on':
        fields.append('name');
    email = request.values.get("email")
    if email == 'on' or varall == 'on':
        fields.append('email')
    contact_no = request.values.get("contact_no")
    if contact_no == 'on' or varall == 'on':
        fields.append('contact_no')
    skills = request.values.get("skills")
    if skills == 'on' or varall == 'on':
        fields.append('skills')
    experience = request.values.get("experience")
    if experience == 'on' or varall == 'on':
        fields.append('experience')
    # 'on' if checked else 'None' 
    query_json = {'query':{'simple_query_string': { 'query': search,'fields':fields}}}
    es_results = es.search(index="student",body=query_json,size=10)
    es_result_hits = es_results['hits']
    search_rec = []
    if es_result_hits["total"]["value"] > 0  :
        for searchResult in es_result_hits["hits"] :
            search_rec.append(searchResult["_source"])

    return render_template('elasticsearch.html',todos=search_rec,flag=True)

@elasticSearch.route("/elasticsearch")
def elastic ():
    return render_template('elasticsearch.html',todos="",flag=False)
