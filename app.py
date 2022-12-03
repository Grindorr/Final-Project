#Importando as bibliotecas
from  flask import Flask, render_template, request
import pandas as pd
import csv
from uuid import uuid4

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

#salva as as variaveis em uma nova row no arquivo.csv
@app.route('/salvar', methods=['POST'])
def salvar():

    #pega as variaveis do forms
    name = request.form['name']
    status = request.form['status']

    lista = []
    lista.append([uuid4(), name, status])

    #faz um append na nova row em .csv
    with open('livros.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(lista)

    #manda para "/"
    with open('livros.csv', 'rt') as file_in:
        livros = csv.DictReader(file_in)
        return render_template('home.html', livros=livros)


#ira deletar rows de acordo com id gerado acima com a biblioteca uuid
app.route('/deletar/<id>')
def deletar(id):

    #usa o pandas para abrir o arquivo csv
    data = pd.read_csv('livros.csv')
    #seta o valor do index para a coluna 'id'
    data = data.set_index('Id')

    #joga toda row que tiver a mesma variavel "id" na coluna index
    data.drop(id, axis='index', inplace=True)

    #salva o novo dataset
    data.to_csv('livros.csv')

    #função que ira ler o arquivo e assimm enviar a variavel para o html
    with open('livros.csv', 'rt') as file_in:
        livros = csv.DictReader(file_in)
        return render_template('home.html', livros=livros)


#ira pegar as variaveis que o usuario quer modificar e coloca dentro do forms
@app.route('/edit/<id>/<name>/<status>')
def edit(id,name,status): #pega as variaveis pela url
    lista2 = [id, name, status] #tranformara em lista para facilitar a manutenção
    return render_template('edit.html', lista2=lista2) # e envia para edit.html


#ira salvar o forms que for modificado no /edit/
@app.route('/salvarup', methods=['POST'])
def salvarup():

    #pegas as novas variaveis
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']

    #ira abrir o dataframe do .csv
    data = pd.read_csv('livros.csv')

    #ira criar um novo dataframe usando as novas variaveis
    novo_dataframe = pd.DataFrame({'Id': [id], 'name': [name], 'status': [status]})

    #ira setar o index para a coluna id
    data = data.set_index('Id')
    novo_dataframe = novo_dataframe.set_index('Id')

    #ira atualizar os dados do antigo data frame com o novo
    data.update(novo_dataframe)

    #salvando o  arquivo
    data.to_csv('livros.csv')

    #ira  direcionar para '/'
    with open('livros.csv', 'rt') as file_in:
        livros = csv.DictReader(file_in)
        return render_template('home.html', livros=livros)

app.run(debug=True)
