# edgelist2graph.py by Adam G. Craig, 2026-08-20
# Load the a list of edges from a CSV file.
# Convert it to a WalkableGraph object.
# Save it to a pickle file.

import argparse
import csv
import pickle
from mbrw import WalkableGraph

def getarguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--edgelistfile', type=str, default='smallnetwork.csv', help='path to the input edge list CSV file')
    parser.add_argument('--graphfile', type=str, default='smallnetwork.pkl', help='path to the output graph pickle file')
    args = parser.parse_args()
    edgelistfile = args.edgelistfile
    graphfile = args.graphfile
    return edgelistfile, graphfile

def loadedgelist(edgelistfile:str):
    edgelist = []
    with open(edgelistfile, 'r') as f:
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
edgelistfile, graphfile = getarguments()
print('loading edge list from file:', edgelistfile)
edgelist = loadedgelist(edgelistfile=edgelistfile)
print('constructing WalkableGraph object from edge list')
graph = WalkableGraph(edgelist=edgelist)
numnodes = graph.getnumnodes()
numedges = graph.getnumedges()
print(f'The graph contains {numnodes} nodes and {numedges} edges.')
print('retrieving edge list from WalkableGraph object')
newedgelist = graph.getedgelist()
compareedgelists(edgelist=edgelist, newedgelist=newedgelist)
print('saving graph to file:', graphfile)
with open(graphfile, 'wb') as graphfilewrite:
    pickle.dump(obj=graph, file=graphfilewrite)
print('done')