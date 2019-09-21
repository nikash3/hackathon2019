from flask import Blueprint, render_template
from elasticsearch import Elasticsearch

elasticSearch = Blueprint('elasticSearch', __name__)

@elasticSearch.route("/search")
def action ():
    HOST_URLS = ["http://127.0.0.1:9200"]
    es_conn = Elasticsearch(HOST_URLS)
    INDEX_NAME = "myproject"
    TYPE_NAME_USER = "user"
    res = es_conn.indices.create(index= INDEX_NAME, ignore=400)
    return "Cluster Name: " + es_conn.cluster.state(metric=["cluster_name"])['cluster_name']
