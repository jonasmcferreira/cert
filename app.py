#!/usr/bin/env python3
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/exam')
def exam():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    try:
        with open('questions.json', 'r') as f:
            questions = json.load(f)
        return jsonify(questions)
    except FileNotFoundError:
        return jsonify({})



if __name__ == '__main__':
    app.run(debug=True)