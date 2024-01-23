class Graph_AS:
    def __init__(self):
        """Inititate graph"""
        self.V = set()
        self.nbrs = dict()
    
    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        """Add Vertex"""
        self.V.add(v)
        
    def remove_vertex(self, v):
        """Remove Vertex"""
        self.V.remove(v)

    def add_edge(self, e):
        """Add Edge"""
        a, b = e # e = (vertex1, vertex2)
        if a not in self.nbrs:
            self.nbrs[a] = {b}
        else:
            self.nbrs[a].add(b)

    def remove_edge(self, e):
        """Remove Edge"""
        a, b = e
        self.nbrs[a].remove(b)
        if len(self.nbrs[a]) == 0:
            self.nbrs.pop(a)

    def _neighbors(self, v):
        """Iterates neighbors"""
        return iter(self.nbrs[v]) if v in self.nbrs else set()
