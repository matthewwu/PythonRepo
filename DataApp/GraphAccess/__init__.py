__author__ = 'mwu'

from bulbs.titan import Graph, Config
from bulbs.rexster import RexsterClient
from bulbs.rexster import index
from bulbs.property import String, Integer, DateTime,Long

'''
config = Config("http://localhost:8182/graphs/graph")

g = Graph(config)


from_v1 = g.vertices.create(Eid=5700000000003,db="CR",TYPE=0,Sid=8200000000002)
from_v2 = g.vertices.create(Eid=5700000000003,db="CR",TYPE=0,Sid=8200000000002)
from_v3 = g.vertices.create(Eid=5700000000003,db="CR",TYPE=0,Sid=8200000000002)
to_v1 = g.vertices.create(Eid=9001174, db="CDDB", TYPE=0, Sid=0)
to_v2 = g.vertices.create(Eid=9540648, db="CDDB", TYPE=0, Sid=0)
to_v3 = g.vertices.create(Eid=24853323, db="CDDB", TYPE=0, Sid=8200000000315)


g.edges.create(from_v1,"Link",to_v1,L_Type="D",SCORE=99)
g.edges.create(from_v2,"Link",to_v2,L_Type="D",SCORE=100)
g.edges.create(from_v3,"Link",to_v3,L_Type="D",SCORE=99)


client = RexsterClient(config)
e = client.get_all_edges()


script = client.scripts.get("get_vertices")
print(script)
response = client.gremlin(script,params=None)
print(response)
result = response.results
for r in result:
    print(r.get_data())
'''