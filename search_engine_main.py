# main.py or your Flask application file

from flask import Flask, render_template, request, redirect, url_for
from utils.ques1.search_engine import SearchEngine



app = Flask(__name__)
search_engine = SearchEngine(index_file='data/publications.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            return redirect(url_for('results', query=query))
    return render_template('index.html')

@app.route('/results')
def results():
    query = request.args.get('query')
    results = []
    if query:
        results = search_engine.search(query)
        # Process results
        for result in results:
            authors = result['Authors']
            profile_links = result['Profile Links']
            if len(authors) != len(profile_links):
                profile_links = profile_links[:len(authors)]
            result['AuthorProfilePairs'] = list(zip(authors, profile_links))
    return render_template('results.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
