from audioop import minmax
from cmath import inf
from struture.node import Node

infinity = float('inf')

class MinMax():

    def __init__(self, next_edges, end_condition, heuristic_function):
        self.next_edges = next_edges
        self.end_condition = end_condition
        self.heuristic_function = heuristic_function

    # https://www.youtube.com/watch?v=l-hh51ncgDI
    def search(self, node: Node, depth: int, maximizing: bool = True, __first__: bool = True, __alpha__: float = -infinity, __beta__: float = infinity):
        if depth == 0 or self.end_condition(node):
            return self.heuristic_function(node)
        
        value:float
        if maximizing:
            value = -infinity
            max_tuple = tuple([-infinity, None])

            for edge in self.next_edges(node):
                eval = max(value, self.search(edge.node, depth - 1, False, False, __alpha__, __beta__))
                value = max(value, eval)
                __alpha__ = max(__alpha__, eval)

                if __first__:
                    if value > max_tuple[0]:
                        max_tuple = tuple([value, edge])
                
                if __beta__ <= __alpha__:
                    break

            if __first__:
                return max_tuple[1].node

        else:
            value = infinity
            for edge in self.next_edges(node):
                eval = min(value, self.search(edge.node, depth - 1, False, False, __alpha__, __beta__))
                value = min(value, eval)
                __beta__ = min(__beta__, eval)
                if __beta__ <= __alpha__:
                    break

        return value
