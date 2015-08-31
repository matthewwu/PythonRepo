import time

from GraphAccess.TitanAccess import TitanAccess
from SQLAccess.LinkResultAccess import Link_Result_Access
from SQLAccess.LinkResultAccess import Link_Result



def load_data_to_graph(start,batch,titanUrl):
    maxFromId = 0
    linkResults = load_data(start,batch)
    if(len(linkResults) > 0):
        maxFromId = save_data(linkResults,titanUrl)

    return maxFromId


def load_data(start,batch):
    linkResultAccess = Link_Result_Access("dms-cr-3","crlinking","LinkResultsService","WeeblesW0bble")
    linkResults = linkResultAccess.get_link_result(start,batch)
    return linkResults


def save_data(linkResults,titanUrl):
    titanAccess = TitanAccess(titanUrl)
    max = 0
    current_out_id = 0
    current_vout = None
    vOut = None
    for item in linkResults:
        if(item.from_id > max):
            max = item.from_id
        vOutProperties = item.getFromProperties()
        vInProperties = item.getToProperties()
        eProperties = item.getEdgeProperties()
        if(item.from_id == current_out_id):
            vOut = current_vout
        else:
            vOut = titanAccess.getOrCreateVertex('Eid',item.from_id,**vOutProperties)
            current_out_id = item.from_id
            current_vout = vOut
        vIn = titanAccess.getOrCreateVertex('Eid',item.to_id,**vInProperties)
        edge = titanAccess.createEdge(vOut,'Link',vIn,**eProperties)
    return max


def run(start,batch,url="http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph"):
    completed = 0
    while start >0:
        start_time = time.time()
        start = load_data_to_graph(start,batch,url)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        print(start)
        completed = completed + batch
        print(completed)
    '''
    57000000082904
    '''