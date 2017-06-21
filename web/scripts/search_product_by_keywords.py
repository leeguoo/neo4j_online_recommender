from py2neo import Graph, NodeSelector
from py2neo import Node, Relationship

graph = Graph(password="123456")

def search_product_by_keywords(keywords):
    selector = NodeSelector(graph)
    selected = []

    by_title = selector.select("Product")\
                       .where("_.title =~ '.* {0} .*'".format(keywords))\
                       .limit(12)
    selected += list(by_title)

    if len(selected)<12:
        by_dscrp = selector.select("Product")\
                           .where("_.description =~ '.* {0} .*'".format(keywords))\
                           .limit(12-len(selected))

        selected += list(by_dscrp)

    return list(selected)

#print(search_product_by_keywords("stroller"))
