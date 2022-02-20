from struture.stack import Stack
from struture.nome import Node

class DepthFirstSearch:

    def __init__(self, stop_condition, generate_next=None):
        self.__stop_condition__= stop_condition
        self.__generate_next__= generate_next
        self.__stack__ = Stack()
        self.__visiteds__= []

    def __autogen_get_path__(self):
        return
    
    def __get_path__(self, node: Node):
        self.__stack__
        return

    def get_path(self, node: Node) -> []:
        path = []
        if self.__generate_next__:
            path = self.__autogen_get_path__()
        else:
            path = self.__get_path__
        
        self.__visiteds__.clear()
        return path

    

