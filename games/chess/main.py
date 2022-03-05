from chess import Board
from struture.node import Edge, Node

def __calculate_cost__(board: Board):
    return 0

def generate_next(node: Node):
    board: Board = node.content
    for move in list(board.legal_moves):
        board_copy = board.copy()
        board_copy.push(move)
        node.edges.append(Edge(board_copy, __calculate_cost__(board_copy)))

def start():
    evalu
    pass

board = Board()
generate_next(board)