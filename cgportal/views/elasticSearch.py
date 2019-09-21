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
        record = { "name": todo["name"], "file": todo["file"], "email": todo["email"], "skills": todo["skills"] , "contact_number" : todo["contact_number"]}
        es.index(index="student", doc_type="student-resume", id=todo["_id"],body=record)

@elasticSearch.route("/elastic_search", methods=['POST'])
def elasticsearch ():
    search = request.values.get("searchname")
    name = request.values.get("name")
    email = request.values.get("email")
    contact_no = request.values.get("contact_no")
    skills = request.values.get("skills")
    experience = request.values.get("experience")
    # 'on' if checked else 'None' 
    query_json = {'query':{'simple_query_string': { 'query': search,'fields':['skills']}}}
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