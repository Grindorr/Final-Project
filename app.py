#Importando as bibliotecas
from  flask import Flask, render_template, request
import pandas
import csv
import uuid 

app = Flask(__name__)


#le os livros.csv e manda para home.html
@app.route('/')
def home():
    with open('livros.csv', 'rt') as file_in:
        livros = csv.DictReader(file_in)
        return render_template('home.html', livros=livros)

#Não lembro como funciona
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    status = request.form['status']
    task = {'name': name, 'status': status}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)


app.run(debug=True)
