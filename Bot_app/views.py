from flask import Flask, render_template, request, json
from Bot_app.parser import Parser

app = Flask(__name__)

app.config.from_object("config")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    questiont = request.form['question']
    Parser(questiont)
    return questiont
