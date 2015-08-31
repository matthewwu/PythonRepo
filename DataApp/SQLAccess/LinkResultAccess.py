__author__ = 'mwu'

from os import getenv
import pymssql
import _mssql

class Link_Result_Access:
    '''
    Interface to work on link result sql
    '''
    def __init__(self,server,db,user,password):
        self.server = server
        self.user = user
        self.password = password
        self.db = db

    def get_link_result(self,start_id,batch):
        lrCollection = []
        counter = 1
        server = getenv(self.server)
        user = getenv(self.user)
        password = getenv(self.password)

        try:
            conn = pymssql.connect(self.server, self.user, self.password, self.db)
            cursor = conn.cursor()

            script = 'SELECT link_id,from_id,from_db,from_source_id,' \
                     'to_id,to_db,to_source_id,link_type,link_score,from_media_id FROM link_results with (nolock) where from_id > {0} order by FROM_id'.format(start_id)
            cursor.execute(script)
            row = cursor.fetchone()
            while row:

                lr = Link_Result()
                lr.link_id = row[0]
                lr.from_id = row[1]
                if(row[2] is not None):
                    lr.from_db = row[2]
                if(row[3] is not None):
                    lr.from_source_id = row[3]
                if(row[4] is not None):
                    lr.to_id = row[4]
                if(row[5] is not None):
                    lr.to_db = row[5]

                if(row[6] is not None):
                    lr.to_source_id = row[6]
                if(row[7] is not None):
                    lr.link_type = row[7]
                lr.link_score = row[8]

                if(row[9] is not None):
                    lr.from_media_id = row[9]

                if(lr.to_id > 0):
                    lrCollection.append(lr)

                row = cursor.fetchone()
                counter = counter + 1

                if(counter > batch):
                    break
        except _mssql.MssqlDatabaseException as e:
            raise
        finally:
            conn.close()
        return lrCollection


class Link_Result:
    def __init__(self):
        self.link_id = 0
        self.from_id = 0
        self.to_id = 0
        self.from_db = ""
        self.to_db = ""
        self.from_source_id = 0
        self.link_type = ""
        self.to_source_id = 0
        self.link_score = 0
        self.from_media_id = 0

    def getFromProperties(self):
        return {'Eid':self.from_id,'db':self.from_db,'Sid':self.from_source_id,'Mid':self.from_media_id}

    def getToProperties(self):
        return {'Eid':self.to_id,'db':self.to_db,'Sid':self.to_source_id}

    def getEdgeProperties(self):
        return {'L_Type':self.link_type,'SCORE':self.link_score}