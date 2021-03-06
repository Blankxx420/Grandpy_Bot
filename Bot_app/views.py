from flask import render_template, request
from Bot_app.parser import Parser
from Bot_app import app
from Bot_app.map import Map
from Bot_app.wiki import Wiki


@app.route('/')
@app.route('/index')
def index():
    """base route"""
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    """route for get a question and return data for index.js"""

    question_text = request.form['question']
    parser = Parser(question_text)
    geo_map = Map(parser.parsed_question)
    if geo_map.latitude is None or geo_map.longitude is None:
        return {"content": "Missing coordinates"}
    wiki = Wiki(geo_map.longitude, geo_map.latitude)
    if wiki is None:
        return {"content": "No wiki details found"}
    else:
        return {
            "sentence": wiki.json_result["sentence"],
            "url": wiki.json_result["url"],
            "longitude": geo_map.longitude,
            "latitude": geo_map.latitude
        }
