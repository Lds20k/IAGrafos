from struture.node import Node

class DepthFirstSearch:

    def __init__(self, stop_condition, generate_next=None):
        self.__stop_condition__= stop_condition
        self.__generate_next__= generate_next
        self.__visiteds__= []

    def __autogen_get_path__(self, node:Node):
        if self.__stop_condition__(node.content) : return [node.content]

        nexts_edges = self.__generate_next__(node)

        for edge in nexts_edges:
            if edge[0] not in self.__visiteds__:
                self.__visiteds__.append(edge[0])
                solution = self.__autogen_get_path__(edge[0])
                if solution is not None:
                    return solution.insert(0, edge[0])

        return None
        

    def get_path(self, node:Node):
        path = []
        if self.__generate_next__:
            path = self.__autogen_get_path__(node)
        
        self.__visiteds__.clear()
        return path