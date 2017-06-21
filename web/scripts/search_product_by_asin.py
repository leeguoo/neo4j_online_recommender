from py2neo import Graph, NodeSelector
from py2neo import Node, Relationship

graph = Graph(password="123456")

def search_product_by_asin():
    selector = NodeSelector(graph)
    node = selector.select("Product",asin="B000MQSJG4")
    return list(node)[0]

#print(search_product_by_asin())
