import unittest
from GraphAccess.Graph import GraphBase


class GraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = GraphBase()
        self.graph.execute_query('g.V.remove')
        self.graph.execute_query('g.E.remove')

    def create_node_test(self):
        script = """
        def v1=g.addVertex([prop:vp1])
        def v11=g.addVertex([prop:vp1])
        def e1=g.addEdge(v1,v11,'conn',[prop:ep1])
        def v12=g.addVertex([prop:vp1])
        def e2=g.addEdge(v1,v12,'conn',[prop:ep1])
        def v13=g.addVertex([prop:vp1])
        def e3=g.addEdge(v1,v13,'conn',[prop:ep1])
        return [[v1,v11,v12,v13],[e1,e2,e3]]
        """
        param = {'vp1':'profile','ep1':'like'}
        rb = self.graph.execute_query(script,param)
        source_id = rb[0][0]['_id']
        v_ids = [item['_id'] for item in rb[0]]
        v_ids = v_ids[1:]

        script="""
        for (i in 0..<d_id.size()){
            g.v(s_id).outE.inV.retain([g.v(d_id[i])]).back(2).remove()
        }
        """
        p={'s_id':1280,'d_id':v_ids}

        s = """
        e=g.v(1280).outE
        return e"""
        p={'s_id':1280,'d_id':v_ids}
        r=g.execute_query(s,p)



if __name__ == '__main__':
    unittest.main()