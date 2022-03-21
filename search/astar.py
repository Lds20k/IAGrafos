import sys

from struture.node import Edge, Node
from struture.priority_queue import PriorityQueue

sys.setrecursionlimit(10000)
class AStarSearch:

    def __init__(self, stop_condition, generate_next, calculate_heuristic):
        self.__stop_condition__ = stop_condition
        self.__generate_next__ = generate_next
        self.__calculate_heuristic__ = calculate_heuristic

    def __autogen_search__(self, queue: PriorityQueue, visiteds: list = []):
        qedge: Edge = queue.pop()
        if qedge is None:
            return None
        node = qedge.node

        visiteds.append(node)
        
        edges = self.__generate_next__(node, self.__calculate_heuristic__)
        for edge in edges:
            next_node: Node = edge.node
            if(not visiteds.__contains__(next_node) and not queue.queue.__contains__(next_node)):
                next_node.set_edge_ant(edge)
                edge.set_node_ant(node)
                if self.__stop_condition__(next_node):
                    return next_node
                queue.push(edge)
        
        return self.__autogen_search__(queue, visiteds)
            

    def search(self, node: Node):
        if self.__stop_condition__(node):
            return node
        queue = PriorityQueue()
        queue.push(Edge(node, 0))
        return self.__autogen_search__(queue, [])
