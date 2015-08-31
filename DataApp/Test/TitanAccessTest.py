__author__ = 'mwu'
import Test
from GraphAccess.TitanAccess import TitanAccess


class TitanAccessTest(Test.TestCase):

    def test_getOrcreateVertex(self):

        titanAccess = TitanAccess("http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph")
        outProperty = {'Eid':2000000000003,'db':'CR','Sid':8200000000002}
        v = titanAccess.createVertex(**outProperty)
        self.assertIsNotNone(v._id)
        j = titanAccess.getOrCreateVertex('Eid',2000000000003,**outProperty)
        self.assertIsNotNone(v._id,j._id)

        titanAccess.deleteVertex(v._id)

'''
    def test_createVertex(self):

        titanAccess = TitanAccess("http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph")
        outProperty = {'Eid':9000000000003,'db':'CR','Sid':8200000000002}
        v = titanAccess.createVertex(**outProperty)
        self.assertIsNotNone(v._id)

        titanAccess.deleteVertex(v._id)


    def test_createEdge(self):
            titanAccess = TitanAccess("http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph")
            outProperty = {'Eid':9000000000003,'db':'CR','Sid':8200000000002}
            vOut = titanAccess.createVertex(**outProperty)
            self.assertIsNotNone(vOut._id)
            inProperty = {'Eid':53535,'db':'CDDB','Sid':8200000000002}
            vIn = titanAccess.createVertex(**inProperty)
            self.assertIsNotNone(vIn._id)
            eProperty = {'SCORE':65}
            e = titanAccess.createEdge(vOut,'Link',vIn,**eProperty)
            self.assertIsNotNone(e._id)
            titanAccess.deleteEdge(e._id)
            titanAccess.deleteVertex(vOut._id)
            titanAccess.deleteVertex(vIn._id)


     def test_createEdgeWithScript(self):
        titanAccess = TitanAccess("http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph")
        outProperty = {'Eid':9000000000003,'db':'CR','Sid':8200000000002}
        vOut = titanAccess.createVertex(**outProperty)
        self.assertIsNotNone(vOut._id)
        inProperty = {'Eid':53535,'db':'CDDB','Sid':8200000000002}
        vIn = titanAccess.createVertex(**inProperty)
        self.assertIsNotNone(vIn._id)
        eProperty = {'SCORE':65}
        e = titanAccess.createEdgeWithScript(vOut,'Link',vIn,65)
        self.assertIsNotNone(e._id)
        titanAccess.deleteEdge(e._id)
        titanAccess.deleteVertex(vOut._id)
        titanAccess.deleteVertex(vIn._id)












    def test_index(self):
        titanAccess = TitanAccess("http://localhost:8182/graphs/graph")
        outProperty = {'test_notunique':9000000000003}
        v = titanAccess.createVertex(**outProperty)
        self.assertIsNotNone(v._id)

'''
if __name__ == '__main__':
    Test.main()