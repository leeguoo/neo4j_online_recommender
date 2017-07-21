# Graph-Based Real-Time Recommender System

In this project, I built a graph-based real-time recommender system to assist online shoppers finding their target products. The basic assumptions are:

The target products are related to the products being browsed.
The more browsed products a product is related to, the higher probability it is the target product.
The more recent the browsed products a product is related to, the higher probability it is the target product. 

With these assumptions, the model well catches the important features of the target products and the change of customers’ ideas.

## Data and Database

The data are from (https://jmcauley.ucsd.edu/data/amazon/). They are stored in a Neo4j graph database. 

## Model

The model is composed of two customized functions stored in web/scripts/search_product_by_asin.py and web/scripts/find_related_asins.py. The recommended products and their weights are stored in rank.json.

The script web/scripts/search_product_by_keywords.py is used to search products by keywords at the beginning. 

## Front End

The web app was built with Flask. 

## Demo

[![Demo](https://github.com/leeguoo/neo4j_online_recommender/blob/master/image/screen_shot_recommender.png?raw=true)](https://youtu.be/NSiL2jWYr54)
