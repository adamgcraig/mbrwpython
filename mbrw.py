class WalkableGraph:

    def __init__(self, edgelist:list):
        endpointlist = []
        for edge in edgelist:
            endpointlist.append(edge[0])
            endpointlist.append(edge[1])
        # print('endpointlist:', endpointlist)
        self.nodelist = list( set(endpointlist) )
        # print('nodelist:', self.nodelist)
        sourcelist = [ edge[0] for edge in edgelist ]
        # print('sourcelist:', sourcelist)
        targetlist = [ edge[1] for edge in edgelist ]
        # print('targetlist:', targetlist)
        sourceidxlist = [ self.nodelist.index(node) for node in sourcelist ]
        # print('sourceidxlist:', sourceidxlist)
        targetidxlist = [ self.nodelist.index(node) for node in targetlist ]
        # print('targetidxlist:', targetidxlist)
        numnodes = len(self.nodelist)
        # print('numnodes:', numnodes)
        numedges = len(edgelist)
        # print('numedges:', numedges)
        self.targetidxlistlist = [  [ targetidxlist[edgeidx] for edgeidx in range(numedges) if sourceidxlist[edgeidx] == sourceidx ] for sourceidx in range(numnodes)  ]
        # print('targetidxlistlist:', self.targetidxlistlist)
        return

    def getnumnodes(self):
        return len(self.nodelist)

    def getnumedges(self):
        return sum([ len(targetidxlist) for targetidxlist in self.targetidxlistlist ])
    
    def getedgelist(self):
        newtargetidxlist = sum(self.targetidxlistlist, [])
        # print('newtargetidxlist:', newtargetidxlist)
        sourceidxlistlist = [  [ idx ]*len(targets) for idx, targets in enumerate(self.targetidxlistlist)  ]
        # print('sourceidxlistlist:', sourceidxlistlist)
        newsourceidxlist = sum(sourceidxlistlist, [])
        # print('newsourceidxlist:', newsourceidxlist)
        newtargetlist = [ self.nodelist[idx] for idx in newtargetidxlist ]
        # print('newtargetlist:', newtargetlist)
        newsourcelist = [ self.nodelist[idx] for idx in newsourceidxlist ]
        # print('newsourcelist:', newsourcelist)
        # Use tuples for edges so that we can use the tuple == operator.
        newedgelist = [ (source, target) for (source, target) in zip(newsourcelist, newtargetlist) ]
        # print('newedgelist:', newedgelist)
        return newedgelist
    