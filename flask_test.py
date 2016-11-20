from flask import Flask
from flask_elasticsearch import FlaskElasticsearch
import json

es = FlaskElasticsearch()
app = Flask(__name__)
es.init_app(app)

@app.route('/')

def search():
    with app.app_context():
        return json.dump(es.search(index="mbdb", body={"query": {"match_all": {}}}), indent=4)
