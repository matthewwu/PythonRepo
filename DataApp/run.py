__author__ = 'mwu'
from App import App

import sys

start = input('Enter a start id: ' )
batch = input('Enter a batch size: ' )
url = input('Enter node ,1,2,3: ')
if(url=="1"):
    url = "http://dms-ps-node-1.globix-sc.gracenote.com:8182/graphs/graph"
else:
    url = "http://dms-ps-node-2.globix-sc.gracenote.com:8182/graphs/graph"

'''57000000083005'''

App.run(int(start),int(batch),url)
