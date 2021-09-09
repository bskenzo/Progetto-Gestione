from flask import Flask, render_template, request
from whoosh.highlight import highlight
import query
import os
import json

app = Flask(__name__)
data = []
headings = ("Title", "Plot", "Director", "Genre", "Data", "Link")

lista_director = []
f = open('director.txt', 'r+', encoding='utf-8')
for name in f.readlines():
    lista_director.append(name)
lista_director = list(set(lista_director))


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/advanced', methods=['GET', 'POST'])
def advanced():
    return render_template('advanced.html', data=lista_director)


@app.route('/results', methods=['GET', 'POST'])
def results():
    ask = {'text': request.args.get('barra'), 'imdb': request.args.get('IMDB'), 'themovie': request.args.get('THEMOVIE'),
           'filmsomniac': request.args.get('FILMSOMNIAC'), 'from': request.args.get('Da'), 'to': request.args.get('a'),
           'director': request.args.get('director')}

    count = request.args.get('n_res')
    if count is None:
        count = 8
    else:
        count = int(count)

    data,lunghezza = query.my_query(ask,count)
    syn = query.expansion_query(ask['text'])
    return render_template("results.html", headings=headings, data=data, syns=syn, lun=lunghezza, syn_lun=len(syn))


if __name__ == "__main__":
    app.run(debug=True)
