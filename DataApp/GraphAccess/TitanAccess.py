__author__ = 'mwu'

from bulbs.titan import Graph, Config
from bulbs.rexster import RexsterClient

class TitanAccess:
    '''
    Interface to work on graph
    '''
    def __init__(self,restUrl):
        self.url = restUrl
        self.config = Config(self.url)
        self.graph = Graph(self.config)

    def getVertex(self):
        v = self.graph.vertices.get()
        return v

    def getOrCreateVertex(self,key,value,**kwds):
        v = self.graph.vertices.get_or_create(key,value,**kwds)
        return v

    def createVertex(self,**kwds):
        v = self.graph.vertices.create(**kwds)
        return v

    def createEdge(self,outV,label,inV,**kwds):
        e = self.graph.edges.create(outV,label,inV,**kwds)
        return e

    def createEdgeWithScript(self,outV,label,inV,score):
        edge_script = "g.addEdge(g.v(o_id),g.v(i_id),'Link',[SCORE:link_score])"
        params = dict(o_id= outV._id, i_id= inV._id,link_score= score)
        edges = self.graph.gremlin.query(edge_script,params)
        return edges

    def deleteVertex(self,vId):
        self.graph.vertices.delete(vId)

    def deleteEdge(self,eId):
        self.graph.edges.delete(eId)

