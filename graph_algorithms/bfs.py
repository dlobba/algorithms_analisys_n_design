#! /usr/bin/python2
import csv, sys, traceback
from Node import Node
from Queue import Queue
#import pdb

def make_adjacent_array (sequence = None):
    adj_array = list()
    for row in sequence:
        node = Node (row[0], row[1:] )
        adj_array.append(node)
    return adj_array

def getAssociatedNode (graph, value):
    for node in graph:
        if node.value == value:
            return node
    return None

def breadth_first_search (graph, root):
    graph_t = [node for node in graph if node != root]
    for node in graph_t:
        node.color = "white"
        node.distance = float('inf')
        node.parent = None
        
    root.color = "gray"
    root.distance = 0
    root.parent = None
    
    Q = Queue ()
    
    print "Start conditions:"
    print ("graph: " + str(graph))
    print ("Q: " + str(Q))
    
    Q.enqueue (root)
    # pdb.set_trace()
    while not Q.isEmpty():
        print "Iteration:"
        u = Q.dequeue ()
        for node in u.adjacent:
            v = getAssociatedNode(graph, node)
            if v.color == "white":
                v.color = "gray"
                v.distance = u.distance + 1
                v.parent = u
                Q.enqueue (v)
            print ("graph: " + str(graph))
            print ("Q: " + str(Q))
        u.color = "black"
    
if __name__ == "__main__":
    try:
        f = open (str(sys.argv[1]), 'rb')
        reader = csv.reader(f, delimiter = ";")
        
        vertex_sequences = list()
        for line in reader:
            vertex_sequences.append(line)
        
        adj_array = (make_adjacent_array (vertex_sequences))
        breadth_first_search (adj_array, adj_array[2])
        
    except Exception as e:
        print (traceback.format_exc(e))
