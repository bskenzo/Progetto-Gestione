from whoosh.qparser import MultifieldParser, OrGroup, QueryParser, WildcardPlugin
from whoosh.qparser.dateparse import DateParserPlugin
from whoosh.index import open_dir
from whoosh.query import Variations
from whoosh import scoring, sorting

# Funzione filtro che seleziona la sorgente delle informazioni 
def source_filter(query, ix):
    
    # Parserizzo solo i link
    qparser = QueryParser("Fpath", ix.schema)
    # Utilizzo il WildcardPlugin per metchare le sorgenti nei link
    qparser.add_plugin(WildcardPlugin()) 

    imdb = ""
    themovie = ""
    filmsomniac = ""

    # Se l'utente seleziona IMDB imposto la variabile imdb a contenere tutti i link che contengono www.imdb.com
    if query['imdb']:  # if the user wants articles from ESA
        imdb = "*www.imdb.com*"

    # Se l'utente seleziona THE MOVIE imposto la variabile themovie a contenere tutti i link che contengono www.themovie.org
    if query['themovie']:
        themovie = "*www.themoviedb.org*"

    # Se l'utente seleziona FILMSOMNIAC imposto la variabile filmsomniac a contenere tutti i link che contengono www.filmsomniac.com
    if query['filmsomniac']:
        filmsomniac = "*www.filmsomniac.com*"

    # Se non viene fatta alcuna scelta imposto tutte e tre le sorgenti di default 
    if (not query['imdb']) and (not query['themovie']) and (not query['filmsomniac']):
        return qparser.parse("*www.imdb.com* OR *www.themoviedb.org* OR *www.filmsomniac.com*")    
    # Altrimenti parserizzo in OR le sorgenti scelte
    else:
        return qparser.parse(f"({imdb} OR {themovie}) OR {filmsomniac}")

# Funzione filtro che seleziona il regista
def director_filter(query, ix):
    
    # Parserizzo solo i direttori
    qparser = QueryParser("Cdirector", ix.schema)

    # Recupero il direttore dal campo della gui
    director = query['director']

    # Se director contiene None o è una stringa vuota imposto director a None
    if director is None or director == '':
        return None   
    # Altrimenti parserizzo in AND il direttore
    else:
        return qparser.parse(f"({director}")

# Funzione filtro che seleziona la data o un range di date
def date_filter(query):

    # Modifico le date dal formato YYYY-MM-DD al formato YYYYMMDD(senza spazi)
    from_date = str.replace(query['from'], '-', '')
    to_date = str.replace(query['to'], '-', '')

    # Inizializzo il range con le date recuperate dalla gui
    date_range = f"Edate:[{from_date} to {to_date}]"

    # Se è settata solo la data di fine imposto data_range a "to to_date"
    if not from_date and to_date is not None:
        date_range = f"Edate:[to {to_date}]"
    # Altrimenti se è settata solo la data di inizio imposto data_range a "from_date to today"
    elif from_date is not None and not to_date:  # if just the ending date is unset
        date_range = f"Edate:[{from_date} to today]"

    return date_range

# Funzione che risolve la query restituendo i risultati 
def my_query(query):

    # Apro l'index
    ix = open_dir(r"C:\Users\keybl\Desktop\Progetti Python\progetto\indexdir")

    # Creo un parser su più campi (titolo e contenuto) raggruppati in OR e con la ricerca automatica sulla variazione morfologica delle parole
    qp = MultifieldParser(["Atitle","Bcontent","Cdirector"],schema=ix.schema,group=OrGroup,termclass=Variations)
    
    # Aggiungo il pluggin per il parsing della data
    qp.add_plugin(DateParserPlugin(free=True))

    # Recupero il filtro delle sorgenti da passare alla query
    sources = source_filter(query, ix)

    #Recupero il filtro del produttore da passare alla query
    director = director_filter(query, ix)
    
    # Recupero la query dalla gui
    query_text = query['text']
    print("our query " + query_text)

    # Se non abbiamo impostato una data imposto il range a None
    if query['from'] is None or query['from'] == '' and query['to'] == '':
        date_range = None
    # Altrimenti chiamo il filtro e aggiungo la ricerca per data (in AND)
    else:
        date_range = date_filter(query)
        query_text += " AND " + date_range
    
    # If non imposto nessun parametro mi ritorna una lista di dizionari vuota (Controllo utile per advanced)
    if query_text == "" and director is None and query['imdb'] is None and query['themovie'] is None and query['filmsomniac'] is None and date_range is None:
        return [{}] 
  
    # Se abbiamo settato un regista aggiungo la ricerca per regista (in AND)   
    if director is not None:
        query_text = query_text + " AND " + str(director)

    # Parserizzo la query
    q = qp.parse(query_text)
    print("parsed query " + str(q))

    # Se ho settato una data o un range di date ordino i risultati prima per data e poi per score
    if date_range is not None:
        return search_for_date(ix,sources,q)
    # Altrimenti ordino i risultati per score
    else:
        return search(ix,sources,q)

# Funzione che restituisce i risultati ordinati per data
def search_for_date(ix,sources,q):
    lista = []

    # Variabile per fare il sorting sugli score
    scores = sorting.ScoreFacet()

    # Variabile per fare il sorting sulla data
    date = sorting.FieldFacet("Edate")

    # Cerco i match, li aggiungo per chiave ad un dizionario, e poi aggiungo il dizionario a una lista per poi ritornarla alla gui
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=None, filter=sources, terms=True, sortedby=[date,scores])
        results.fragmenter.charlimit = None
        results.fragmenter.maxchars = 300
        results.fragmenter.surround = 10000
        for result in results:
            dicto = {}
            for f in result.fields():
                if f == "Edate":
                    data =  result[f]
                    data = data.date()
                    dicto.update({f"{f}":data})
                else:
                    dicto.update({f"{f}":result[f]})
            dicto["Contenthighlights"] = result.highlights("Bcontent")
            dicto["Titlehighlights"] = result.highlights("Atitle")
            dicto["Directorhighlights"] = result.highlights("Cdirector")
            lista.append(dicto)
    return lista
# "BBhighlights"
# Funzione che restituisce i risultati ordinati per score
def search(ix,sources,q):
    lista = []

    with ix.searcher() as searcher:
        results = searcher.search(q, limit=None, filter=sources, terms=True)
        results.fragmenter.charlimit = None
        results.fragmenter.maxchars = 300
        results.fragmenter.surround = 10000
        for result in results:
            dicto = {}
            for f in result.fields():
                if f == "Edate":
                    data =  result[f]
                    data = data.date()
                    dicto.update({f"{f}":data})
                else:
                    dicto.update({f"{f}":result[f]})
            dicto["Contenthighlights"] = result.highlights("Bcontent")
            dicto["Titlehighlights"] = result.highlights("Atitle")
            dicto["Directorhighlights"] = result.highlights("Cdirector")
            lista.append(dicto)
    return lista

if __name__ == '__main__':
    my_query()