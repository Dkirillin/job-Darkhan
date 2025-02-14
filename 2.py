import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/tictactoe.html')
def tictactoe():
    return render_template('tictactoe.html')

@app.route('/snake.html')
def snake():
    return render_template('snake.html')

app.run(debug=True)

