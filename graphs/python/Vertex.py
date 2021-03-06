class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.distance = 0
        self.predecessor = None
        
    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def add_neighbors(self, neighbors):
        for n in neighbors:
            self.add_neighbor(n)
            
    def get_neighbors(self):
        return self.neighbors

    def get_key(self):
        return self.key

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    def __str__(self):
        return str(self.key) + ' neighbors: ' + str([x.key for x in self.neighbors])


if __name__ == "__main__":
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v1.add_neighbor(v2,5)
    v1.add_neighbor(v3,10)
    v2.add_neighbor(v1,2)

    print v1
    print v2

    assert v1.get_weight(v2) == 5
    assert v1.get_weight(v3) == 10
    assert v2.get_weight(v1) == 2
    assert v1.get_key() == "A"
    assert v1.get_neighbors()[v2] == 5
    assert v1.get_neighbors()[v3] == 10
    

    
