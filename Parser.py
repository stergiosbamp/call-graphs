class Parser:
    def __init__(self):
        self.connected_edges = []

    def parse(self, file):
        for line in file:
            if line[0] == 'C':
                print(line[2:])  # skip first 2 char which are "C:" and take the remaining
                vertex_one, vertex_two = line[2:].strip().split(' ')
                self.connected_edges.append((vertex_one, vertex_two))

        return self.connected_edges
