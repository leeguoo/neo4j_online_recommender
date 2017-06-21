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

@app.route('/', methods=('GET', 'POST'))
def index():
    form = SearchForm()
    result = None

    if form.validate_on_submit():
        submitted_data = form.data
        keywords = submitted_data['keywords']
        result = search_product_by_keywords(keywords)

    return render_template('index.html',
        form=form,
        products=result)


@app.route("/display", methods=["POST"])
def display():
    # Get json data that came with the request
    data = flask.request.json
    print(data)
    #return result as json
    # Put the result in a nice dict so we can send it as json
    results = {"result": 1}
    return flask.jsonify(results)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print(a,b)
    return jsonify(result=a + b)
