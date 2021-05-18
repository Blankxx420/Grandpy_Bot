from flask import Flask, render_template, request
from Bot_app.parser import Parser

app = Flask(__name__)

app.config.from_object("config")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    question_text = request.form['question']
    Parser(question_text)
    return question_text
