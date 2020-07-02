# speed_graph.py
##

class Node():
    def __init__(self):
        self.links = []

    def add_link(self, link):
        if link not in self.links:
            self.links.append(link)

class Graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
        for link in node.links:
            for n in self.nodes:
                if n == link:
                    n.add_link(node)

def create_random_graph(num_of_nodes):
    my_random_graph = Graph()

    nodes = [Node() for i in range(num_of_nodes)]

    for node in nodes:
        for buddy_node in nodes:
            if buddy_node is node:
                pass
            else:
                if random.random() > 0.5:
                    node.add_link(buddy_node)
                    
    for node in nodes:
        my_random_graph.add_node(node)

    return my_random_graph

if __name__ == "__main__":
    import random
    mrg = create_random_graph(4)
    print([node.links for node in mrg.nodes])

