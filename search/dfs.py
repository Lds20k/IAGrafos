from struture.node import Node

class DepthFirstSearch:

    def __init__(self, stop_condition, generate_next=None, generate_id=None):
        self.__stop_condition__ = stop_condition
        self.__generate_next__ = generate_next
        self.__visiteds__ = []
        self.__generate_id__ = generate_id

    def __autogen_search__(self, node: Node, visiteds: list = []):
        if self.__stop_condition__(node.content):
            return [node]

        visiteds.append(node.id())

        nexts_edges = self.__generate_next__(node)

        for edge in nexts_edges:
            if self.__generate_id__(edge) not in self.__visiteds__:
                solution = self.__autogen_search__(edge[0])
                if solution is not None:
                    solution.insert(0, node)
                    return solution

        return None

    def search(self, node: Node):
        path = []
        if self.__generate_next__:
            path = self.__autogen_search__(node)

        self.__visiteds__.clear()
        return path