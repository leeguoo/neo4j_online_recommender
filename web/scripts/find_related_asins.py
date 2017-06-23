from py2neo import Graph, NodeSelector
from py2neo import Node, Relationship

graph = Graph(password="123456")

def find_related_asins(asin):
    cmd = """
          MATCH (a:Product)-[:ALSO_VIEWED]->(b:Product)
          WHERE a.asin='{0}'
          RETURN b.asin
          """.format(asin)
    return graph.run(cmd)
