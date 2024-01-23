class Graph_ES:
    def __init__(self, V = (), E = ()):
        """Inititate graph"""
        self._V = set()
        self._E = set()
        for v in V: self.add_vertex(v)
        for tup in E: self.add_edge(tup)

    def __len__(self):
        return len(self._V)

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, v):
        """Add Vertex"""
        self._V.add(v)

    def remove_vertex(self, v):
        """Remove Vertex"""
        self._V.remove(v)

    def add_edge(self, e):
        """Add Edge"""
        x,y = e
        self._E.add((x,y))

    def remove_edge(self, e):
        """Remove Edge"""
        x,y = e
        self._E.remove((x,y))

    def _neighbors(self, v):
        """Iterates neighbors"""
        return (w for u,w in self._E if u == v)
    