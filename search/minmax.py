from struture.node import Node


from struture.node import Node

class MinMax():

    def __init__(self, next_edges, end_condition, heuristic_function):
        self.next_edges = next_edges
        self.end_condition = end_condition
        self.heuristic_function = heuristic_function

    def search(self, node: Node, depth: int, maximizing: bool):
        
        if depth == 0 and self.end_condition():
            return self.heuristic_function(node.content)
        

