# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Data contoh untuk dicari
sample_data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    # Tambahkan data lain sesuai kebutuhan
]

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        results = search_data(sample_data, search_term)
    else:
        results = []

    return render_template('search.html', results=results)

def search_data(data, term):
    # Fungsi pencarian sederhana
    return [item for item in data if term.lower() in item['name'].lower()]

if __name__ == '__main__':
    app.run(debug=True)
