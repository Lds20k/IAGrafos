class Node:
    def __init__(self, content, edges:list=[]):
        self.content = content
        self.edges:list = edges

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented

        return self.content == other.content
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return str(self.content) + '\n' + str(self.edges)
    
class Edge:
    def __init__(self, node:Node, cost):
        self.node:Node = node
        self.cost = cost
    
    def __str__(self) -> str:
        return str(self.node)

    def __repr__(self) -> str:
        return self.__str__()