class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    #BFS
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
            return False

class adjacency_matrices:
    def __init__(self, data):
        self.graph = data
        self.matrix_elements = sorted(self.graph.keys())
        self.cols = self.rows = len(self.matrix_elements)

    def create_matrix(self):
        adjacency_matrices = [[0 for x in range(self.rows)] for y in range(self.cols)]
        edges_list = []
        
        for key in self.matrix_elements:
            for neighbor in self.graph[key]:
                edges_list.append((key, neighbor))

        for edge in edges_list:
            index_of_first_vertex = self.matrix_elements.index(edge[0])
            index_of_second_vertex = self.matrix_elements.index(edge[1])
            adjacency_matrices[index_of_first_vertex][index_of_second_vertex] = 1
