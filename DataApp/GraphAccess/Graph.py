from rexpro import RexProConnection

class GraphBase(object):

    def __init__(self):
        self.conn = RexProConnection('localhost', 8184, 'graph')


    def execute_query(self, script, params=None):
        self.conn.open()
        r = self.conn.execute(script, params)
        self.conn.close()
        return r
