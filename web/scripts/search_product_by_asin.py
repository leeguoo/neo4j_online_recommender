from py2neo import Graph, NodeSelector
from py2neo import Node, Relationship

graph = Graph(password="123456")

def search_product_by_asin(asin):
    selector = NodeSelector(graph)
    node = selector.select("Product",asin=asin)
    if list(node):
        return list(node)[0]
    return None

#print(search_product_by_asin("B00E4YZY9K"))
