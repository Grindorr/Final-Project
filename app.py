#Importando a biblioteca
from  flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {'name':'Estudar', 'status': 'lido'},
    {'name': 'Dormir', 'status': 'lido'},
    {'name': 'comer', 'status': 'não lido'}
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
