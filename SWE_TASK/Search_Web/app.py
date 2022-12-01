from flask import Flask, render_template, request
from form import SearchForm
from search import Search
import logging
import sys

app = Flask(__name__)
app.secret_key = 'Abc'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm()
    results = []
    if request.method == 'POST': # Submit 
        if form.validate() == False:
            return render_template("index.html", form=form)
        else:
            search_query = form.search_query.data
            book_search = Search(search_query)
            book_search.make_a_search()
            results = book_search.get_search_results()
            return render_template("index.html", form=form, results=results)

    elif request.method == 'GET': # Retrieve results
        return render_template("index.html", form=form, results=results)

if __name__ == '__main__':
    app.run()
