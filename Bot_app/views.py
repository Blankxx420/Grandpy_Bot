from flask import Flask, render_template, request, json

app = Flask(__name__)

app.config.from_object("config")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/question', methods=['POST'])
def question():
    questiont = request.data('questionText')
    return json.dumps({'status': 'ok', 'question': questiont})


