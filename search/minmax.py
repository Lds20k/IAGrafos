from audioop import minmax
from cmath import inf
from struture.node import Node

infinity = float('inf')

class MinMax():

    def __init__(self, next_edges, end_condition, heuristic_function):
        self.next_edges = next_edges
        self.end_condition = end_condition
        self.heuristic_function = heuristic_function

    def search(self, node: Node, depth: int, maximizing: bool = True, __first__: bool = True):
        if depth == 0 or self.end_condition(node):
            return self.heuristic_function(node)
        
        value:float
        if maximizing:
            value = -infinity
            max_tuple = tuple([-infinity, None])

            for edge in self.next_edges(node):
                value = max(value, self.search(edge.node, depth - 1, False, False))
                if __first__ and value > max_tuple[0]:
                    max_tuple = tuple([value, edge])

            if __first__:
                return max_tuple[1].node

        else:
            value = infinity
            for edge in self.next_edges(node):
                value = min(value, self.search(edge.node, depth - 1, False, False))

        return value
