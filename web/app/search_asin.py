from py2neo import Graph, NodeSelector
from py2neo import Node, Relationship

graph = Graph(password="123456")

tmpdict = {}

while True:
    asin = input("INPUT An asin: ")
    cmd = """
          MATCH (a:Product)-[:ALSO_VIEWED]->(b:Product)
          WHERE a.asin='{0}'
          RETURN b.asin
          """.format(asin)

    asins = graph.run(cmd)
    for asin in asins:
        if tmpdict.get(asin,None):
            tmpdict[asin] += 1
        else:
            tmpdict[asin] = 1
    print(tmpdict)
