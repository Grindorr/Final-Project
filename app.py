#Importando a biblioteca
from  flask import Flask, render_template, request
import csv 

app = Flask(__name__)

tasks = [
    {'name':'A culpa é das Estrelas', 'status': 'não lido'},
    {'name': 'Sherlock Holmes', 'status': 'lido'},
    {'name': 'Diario de um banana', 'status': 'não lido'}
]

@app.route('/')
def home():
    # templates/home.html
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    status = request.form['status']
    task = {'name': name, 'status': status}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)


app.run(debug=True)
