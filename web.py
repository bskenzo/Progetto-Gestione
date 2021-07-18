from flask import Flask, render_template, request
import query

app = Flask(__name__)
data = []
headings = ("Title", "Plot", "Director", "Genre", "Data", "Link")

lista_director = []
# Apro il file director.txt per aggiungere i direttori ad una lista da passare alla gui 
with open("director.txt", "r", encoding="utf8") as f:
    for lista in f.readlines():
        lista_director.append(lista)
lista_director = list(set(lista_director))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/advanced', methods=['GET', 'POST'])
def advanced():
    return render_template('advanced.html', data=lista_director)


@app.route('/results', methods=['GET', 'POST'])
def results():
    ask = {'text': request.args.get('barra'), 'imdb': request.args.get('IMDB'), 'themovie': request.args.get('THEMOVIE'), 'filmsomniac': request.args.get('FILMSOMNIAC'),
            'from': request.args.get('Da'), 'to': request.args.get('a'), 'director': request.args.get('director')}
    print(ask)
    data= query.my_query(ask)
    return render_template("results.html", headings=headings, data=data)


if __name__ == "__main__":
    app.run(debug=True)
