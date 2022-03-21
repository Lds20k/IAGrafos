class Node:
    def __init__(self, content, edges:list=[]):
        self.content = content
        self.edges:list = edges
        self.edge_ant: Edge = None
    
    def set_edge_ant(self, ant):
        self.edge_ant: Edge = ant

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented

        return self.content == other.content

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        to_return = f"[{self.content} : {self.edge_ant}]"
        if not self.edge_ant is None:
            to_return = f"{to_return}{self.edge_ant.node_ant}"
        return to_return
    
class Edge:
    def __init__(self, node:Node, value):
        self.node:Node = node
        self.value = value
        self.node_ant: Node = None

    def set_node_ant(self, ant):
        self.node_ant: Node = ant

    def __lt__(self, other):
        return self.value < other.value
    
    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return self.__str__()