class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # this serves as adjacency list
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # checks if vertex_id key already present, if not, populates with empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('ERROR')

def earliest_ancestor(ancestors, starting_node):
    # instantiate graph object
    graph = Graph()
    # loop through ancestors list of tuple pairs 
    # and insert them into the graph as vertices
    for tup in ancestors:
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])
        # reverse tuples to create graph edges
        graph.add_edge(tup[1], tup[0])

    # create Queue to store path
    qq = Queue()
    qq.enqueue([starting_node])
    
    # set up variables 
    max_len = 1
    earliest_ancestor = -1 

    # perform breadth first search, initiate while loop which will terminate once Queue is empty
    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1]

        # checks weather length of path is greater than max length or is equivalent and the vertex value is 
        # less than the earliest ancestor
        if (len(path) > max_len) or (len(path) == max_len and vertex < earliest_ancestor):
            # updates our variables if condition met 
            earliest_ancestor = vertex
            max_len = len(path)
        # for every vertex, loops through neighbors to update path_list
        for neighbor in graph.vertices[vertex]:
            path_list = list(path)
            path_list.append(neighbor)
            qq.enqueue(path_list)
    return earliest_ancestor


