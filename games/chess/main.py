import random
from chess import Board
from struture.node import Edge, Node
from search.minmax import MinMax

def __calculate_cost__(board: Board):
    return 0

def generate_next(node: Node):
    board: Board = node.content
    edges:list = []
    for move in list(board.legal_moves):
        board_copy = board.copy()
        board_copy.push(move)
        edges.append(Edge(Node(board_copy), 0))
    return edges

def is_game_over(node: Node):
    board: Board = node.content
    return board.is_game_over()


def evaluation_heuristic(node: Node):
    board: Board = node.content
    return random.randint(0, 90)
    

def start():
    pass

board = Board()
minmax = MinMax(generate_next, is_game_over, evaluation_heuristic)
node = Node(board)
board.push(minmax.search(node, 2).content.pop())
print(board)