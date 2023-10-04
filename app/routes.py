from app import app
from flask import render_template, request
from .forms import SearchForm
from .api import pokemon_api


@app.route('/', methods=['GET','POST'])
def index(): 
    form = SearchForm()
    if request.method == 'POST':
        if form.validate():
            query = form.query.data

            pokemon = pokemon_api(query)
            if pokemon :
                return render_template('index.html', pokemon=pokemon, form= form)






    return render_template('index.html', form = form)