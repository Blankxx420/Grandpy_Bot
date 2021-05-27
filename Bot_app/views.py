from flask import Flask, render_template, request
from Bot_app.parser import Parser
from Bot_app.map import Map
from Bot_app.wiki import Wiki

app = Flask(__name__)

app.config.from_object("config")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    question_text = request.form['question']
    parser = Parser(question_text)
    geo_map = Map(parser.parsed_question)
    if geo_map.latitude is None or geo_map.longitude is None:
        return {"content": "Missing coordinates"}
    wiki = Wiki(geo_map.latitude, geo_map.longitude)
    if wiki is None:
        return {"content": "No wiki details found"}
    else:
        return {
            "sentence": ["sentence"],
            "url": wiki["url"],
            "longitude": geo_map.longitude,
            "latidude": geo_map.latitude
        }

