# Arrays
# , array is a static data structure (residing in Data or Stack section)
## while linked list is a dynamic data structure (residing in Heap section).
# Graph
# Heap
# Linkedlist
# Queue
# Sorting
# Searching
# Stack
# Trees

class Node:

    def __init__(self, key):
        self.key = key
        self.connections = {}

    def addconnection(self, key, value):
        self.connections[key] = value

    def __str__(self):
        return '{} connections: {}'.format(self.key, [x.key for x in self.connections])

    def getconnections(self):
        return self.connections.keys()

    def getvalues(self, key):
        return self.connections[key]


class Graph:
    """
    Graphs are used to represent networks.  The networks may include paths in a city or telephone network or
    circuit network. Graphs are also used in social networks like linkedIn, Facebook.
     For example, in Facebook, each person is represented with a vertex(or node).
     Each node is a structure and contains information like person id, name, gender, locale etc.
     DFS. BFS, Graph cycle, Topological sorting, minimum spanning tree, backtracking, shortest path, connectivity, maximum flow

    It has 2 components : Nodes (vertices and edges) .
    A finite set of ordered pair of the form (u, v) called as edge.
    The pair is ordered because (u, v) is not same as (v, u) in case of directed graph(di-graph).
    The pair of form (u, v) indicates that there is an edge from vertex u to vertex v.
    The edges may contain weight/value/cost.

    It can be represented using Adjacency Matrix and Adjacency List

    Time Complexities:
    NOTE: AL = Adjacency List, AM = Adjacency Matrix, V = Vertex, E = Edge

    Store Graph: AL: O(|V| + |E|), AM: O(|V| * |V|)
    Add Vertex: AL: O(1), AM: O(|V| * |V|)
    Add Edge: AL: O(1), AM: O(1)
    Remove Vertex: AL: O(|E|), AM: O(|V| * |V|)
    Remove Edge: AL: O(|V|), AM: O(1)

    AL: Slow to remove vertices and edges, because it needs to find all vertices or edges
    AM: Slow to add or remove vertices, because matrix must be resized/copied

    Graph using Adjacency List

    """

    def __init__(self):
        self.items = {}

    # print values in Stack
    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    def printgraph(self):
        for v in self.items:
            print(v, '->', '->'.join([str(i) for i in self.items[i]]))

    def addnode(self, node):
        """

        :type node: object
        """
        self.items[node.key] = node

    def getnode(self, key):
        try:
            return self.items[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.items

    def addedge(self, from_key, to_key, weight=0):
        if from_key not in self.items:
            self.addnode(Node(from_key))
        if to_key not in self.items:
            self.addnode(Node(to_key))
        self.items[from_key].addconnection(self.items[to_key], weight)


    def getallnodes(self):
        return self.items.keys()

    def __iter__(self):
        return iter(self.items.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addnode(Node(i))
    print(g.items)
    g.addedge(0, 1, 5)
    g.addedge(0, 5, 2)
    g.addedge(1, 2, 4)
    g.addedge(2, 3, 9)
    g.addedge(3, 4, 7)
    g.addedge(3, 5, 3)
    g.addedge(4, 0, 1)
    g.addedge(5, 4, 8)
    g.addedge(5, 2, 1)
    print(g.getallnodes())
    for v in g:
        for w in v.getconnections():
            print('{} -> {}'.format(v.key, w.key))
