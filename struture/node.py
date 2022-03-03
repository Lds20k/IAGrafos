class Node:
    def __init__(self, content, edges:list=None):
        self.content = content
        self.edges:list = edges

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented

        return self.content == other.content
    
    def __repr__(self) -> str:
        return str(self.content) + '\n'
    
class Edge:
    def __init__(self, node:Node, cost):
        self.node:Node = node
        self.cost = cost