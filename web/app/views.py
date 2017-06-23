import logging
import json

from flask import request
from flask import render_template
from flask_wtf import FlaskForm as Form
from wtforms import fields
from wtforms.validators import Required, Length
from flask import Flask, jsonify, render_template, request

from . import app #, estimator, target_names


logger = logging.getLogger('app')

class SearchForm(Form):
    keywords = fields.StringField(u'keywords', validators=[Required(),Length(max=50)])
    submit = fields.SubmitField('Submit')

from scripts.search_product_by_asin import search_product_by_asin
from scripts.search_product_by_keywords import search_product_by_keywords
from scripts.find_related_asins import find_related_asins

#@app.route('/', methods=('GET', 'POST'))
#def index():
#    form = SearchForm()
#    result = None
#
#    if form.validate_on_submit():
#        submitted_data = form.data
#        keywords = submitted_data['keywords']
#        result = search_product_by_keywords(keywords)
#
#        f = open('rank.json','w')
#        f.write('{}')
#        f.close()
#
#    return render_template('index.html',
#        form=form,
#        products=result)


@app.route('/', methods=('GET', 'POST'))
def index():
    form = SearchForm()
    result = None

    if form.validate_on_submit():
        submitted_data = form.data
        keywords = submitted_data['keywords']
        result = search_product_by_keywords(keywords)

        f = open('rank.json','w')
        f.write('{}')
        f.close()

    return render_template('index.html',
        products=result)

import json

def UpdateRanking(asin):
    with open('rank.json','r') as f:
        rank = json.load(f)

    related_asins = find_related_asins(asin)
    for related_asin in related_asins:
        key = list(related_asin)[0]
        if key in rank:
            rank[key] += 1
        else:
            rank[key] = 1
    with open('rank.json','w') as f:
        json.dump(rank,f)

@app.route('/display')
def display():
    asin = request.args.get('a', 0, type=str)
    result = search_product_by_asin(asin)
    UpdateRanking(asin)
    return jsonify(result)

import operator
@app.route('/recommend')
def recommend():
    form = SearchForm()
    results = None
    with open('rank.json','r') as f:
        rank = json.load(f)
    results = []
    for item in sorted(rank.items(),key=operator.itemgetter(1))[:12]:
        asin = item[0]
        print(asin)
        results.append(search_product_by_asin(asin))
    return render_template('index.html',
                            form=form, 
                            products=results)
