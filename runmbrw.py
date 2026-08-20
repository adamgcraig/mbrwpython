import argparse
import csv
from mbrw import WalkableGraph

def getnetworkfile():
    parser = argparse.ArgumentParser()
    parser.add_argument('--networkfile', type=str, default='smallnetwork.csv', help='path to the edge list CSV file')
    args = parser.parse_args()
    networkfile = args.networkfile
    return networkfile

def loadedgelist(networkfile:str):
    edgelist = []
    with open(networkfile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            # Use tuples for edges so that we can use the tuple == operator.
            edgelist.append( tuple(row) )
    # print('edgelist:', edgelist)
    numedges = len(edgelist)
    print(f'{numedges} edges in loaded edge list')
    return edgelist

def compareedgelists(edgelist:list, newedgelist:list):
    edgeset = set(edgelist)
    numedges = len(edgeset)
    print(f'{numedges} unique edges are in the original edge list.')
    newedgeset = set(newedgelist)
    numnewedges = len(newedgeset)
    print(f'{numnewedges} unique edges are in the reconstructed list.')
    missing = edgeset.difference(newedgeset)
    nummissing = len(missing)
    print(f'{nummissing} edges are in the original but not the reconstructed list.')
    if nummissing > 0:
        print(missing)
    extra = newedgeset.difference(edgeset)
    numextra = len(extra)
    print(f'{numextra} edges are in the reconstructed list but not in the original.')
    if numextra > 0:
        print(extra)
    return

print('running runmbrw.py...')
networkfile = getnetworkfile()
print('loading edge list from network file:', networkfile)
edgelist = loadedgelist(networkfile=networkfile)
print('constructing WalkableGraph object from edge list')
graph = WalkableGraph(edgelist=edgelist)
numnodes = graph.getnumnodes()
numedges = graph.getnumedges()
print(f'The graph contains {numnodes} nodes and {numedges} edges.')
print('retrieving edge list from WalkableGraph object')
newedgelist = graph.getedgelist()
compareedgelists(edgelist=edgelist, newedgelist=newedgelist)
print('done')