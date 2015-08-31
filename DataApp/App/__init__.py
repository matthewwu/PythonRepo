__author__ = 'mwu'
import time
'''
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
    for item in linkResults:
        if(item.from_id > max):
            max = item.from_id
        vOutProperties = item.getFromProperties()
        vInProperties = item.getToProperties()
        eProperties = item.getEdgeProperties()
        vOut = titanAccess.getOrCreateVertex('Eid',item.from_id,**vOutProperties)
        vIn = titanAccess.getOrCreateVertex('Eid',item.to_id,**vInProperties)
        edge = titanAccess.createEdge(vOut,'Link',vIn,**eProperties)
    return max


def run(start,batch):
    start = 57000000081906
    batch = 1000
    completed = 0
    while start >0:
        start_time = time.time()
        start = load_data_to_graph(start,batch,"http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph")
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        print(start)
        completed = completed + batch
        print(completed)
'''