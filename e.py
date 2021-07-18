from whoosh import fields, index, qparser, sorting
from whoosh.analysis import StemmingAnalyzer

schema = fields.Schema(title=fields.TEXT(stored=True, spelling=True),
                       price=fields.NUMERIC(sortable=True))
ix = index.create_in("indexdir2", schema)

with ix.writer() as w:
    w.add_document(title="Big Deal", price=20)
    w.add_document(title="Mr. Big", price=10)
    w.add_document(title="Big Big Top", price=15)
    w.add_document(title="avengers endgame", price=15)
    w.add_document(title="the avenger", price=15)
    w.add_document(title="launch", price=15)
    # w.add_document(title="avenge line", price=15)

user_query_string = "lar"

with ix.searcher() as s:
    # qp = qparser.QueryParser("title", ix.schema)
    # q = qp.parse(user_query_string)
    qp = qparser.QueryParser("title", ix.schema)
    q = qp.parse(user_query_string)
    print("parsed query " + str(q))
    print("query " + str(user_query_string))

    corrected = s.correct_query(q, user_query_string)
    if corrected.query != q:
        print("Did you mean:", corrected.string)

    facet = sorting.FieldFacet("price", reverse=True)
    cats = sorting.FieldFacet("price")
    scores = sorting.ScoreFacet()

    # Sort search results from lowest to highest price
    results = s.search(q, sortedby=[scores, cats])
    for hit in results:
        print(hit["title"])


# # Sort by the “category” field, then by the document’s score:

# results = searcher.search(myquery, sortedby=[cats, scores])