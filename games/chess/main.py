from cgitb import text
from lib2to3.pytree import convert
import random
from sqlite3 import connect
import chess
import chess.svg
from chess import Board
from struture.node import Edge, Node
from search.minmax import MinMax

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

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

# Valores das peças
piece_values = {
    chess.PAWN:   100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK:   500,
    chess.QUEEN:  900,
    chess.KING:   20000
}

# Calcula o materia de quem é o turno
def calculate_material(board: Board):
    white_material = 0
    black_material = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        if piece.color == chess.WHITE:
            white_material += piece_values[piece.piece_type]
        
        if piece.color == chess.BLACK:
            black_material += piece_values[piece.piece_type]
    return white_material - black_material if board.turn else black_material - white_material

# Peso das posições para cada peça
piece_position_values = {
    chess.PAWN: [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ],
    chess.KNIGHT: [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50
    ],
    chess.BISHOP: [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20
    ],
    chess.ROOK: [
         0,  0,  0,  0,  0,  0,  0,  0,
         5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
         0,  0,  0,  5,  5,  0,  0,  0
    ],
    chess.QUEEN: [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ],
    chess.KING:{
        "MIDDLEGAME":[
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -30,-40,-40,-50,-50,-40,-40,-30,
            -20,-30,-30,-40,-40,-30,-30,-20,
            -10,-20,-20,-20,-20,-20,-20,-10,
             20, 20,  0,  0,  0,  0, 20, 20,
             20, 30, 10,  0,  0, 10, 30, 20
        ],
        "ENDGAME":[
            -50,-40,-30,-20,-20,-30,-40,-50,
            -30,-20,-10,  0,  0,-10,-20,-30,
            -30,-10, 20, 30, 30, 20,-10,-30,
            -30,-10, 30, 40, 40, 30,-10,-30,
            -30,-10, 30, 40, 40, 30,-10,-30,
            -30,-10, 20, 30, 30, 20,-10,-30,
            -30,-30,  0,  0,  0,  0,-30,-30,
            -50,-30,-30,-30,-30,-30,-30,-50
        ]
    }
}

# Retorna a cor do turno
turn_color = lambda turn: "Branco\0" if turn else "Preto\0"

def count_turns(board: Board):
    return board.fullmove_number * 2 + 1 if board.turn else board.fullmove_number * 2 

# considering a game with ten minutes and the mean of 20 seconds for a move
turns_of_middle_game = 15

# Calcula a heuristica
def evaluation_heuristic(node: Node):
    board: Board = node.content
    heuristic_value = calculate_material(board)
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        piece_type = piece.piece_type

        if  piece_type == chess.KING:
            game_turns = count_turns(board)
            position_values = piece_position_values[piece_type]["MIDDLEGAME" if game_turns < turns_of_middle_game else "ENDGAME"]
            if not board.turn: 
                position_values = list(position_values).copy()
                position_values = position_values[::-1]

            heuristic_value += position_values[square]
        else:
            position_values =  piece_position_values[piece_type]
            if not board.turn: 
                position_values = list(position_values).copy()
                position_values = position_values[::-1]
            heuristic_value += position_values[square]

    return heuristic_value

# Inicia o jogo
def start():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    # board = Board()

    # minmax = MinMax(generate_next, is_game_over, evaluation_heuristic)
    # node = Node(board)
    # print(board)

    # while(not board.is_game_over()):
    #     print(board.legal_moves)
    #     move = input("Jogada: ")
    #     board.push_san(move)
    #     print(board)

    #     board.push(minmax.search(node, 4).content.pop())
    #     print(board)

# Janela
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 500)

        self.widgetSvg = QSvgWidget(self)
        self.widgetSvg.setGeometry(0, 0, 500, 500)

        self.chessboard = Board()

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

        self.txtMove = QLineEdit(self)
        self.txtMove.setMaxLength(4)
        self.txtMove.setFont(QFont("Arial", 10))
        self.txtMove.setGeometry(510, 10, 280, 30)

        self.btnJogar = QPushButton(self)
        self.btnJogar.setText("Jogar")
        self.btnJogar.setGeometry(510, 60, 280, 30)
        self.btnJogar.clicked.connect(self.btnJogarOnClick)

        self.tbxLegalMoves = QTextEdit(self)
        self.tbxLegalMoves.setText(self.convert_list_of_moves())
        self.tbxLegalMoves.setGeometry(510, 120, 280, 300)
        self.tbxLegalMoves.setFont(QFont("Arial",10))
        self.tbxLegalMoves.setReadOnly(True)

        self.minmax = MinMax(generate_next, is_game_over, evaluation_heuristic)

        self.setWindowTitle("Xadrez!")

    def convert_list_of_moves(self):
        moves = ""
        i = 1
        print(self.chessboard.legal_moves)
        for move in self.chessboard.legal_moves:
            moves += str(self.chessboard.san(move)) + "\t"
            if i % 4 == 0:
                moves += "\n"
            i += 1
        return moves

    def btnJogarOnClick(self):
        self.chessboard.push_san(self.txtMove.text())

        # ATT Tabuleiro
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

        node = Node(self.chessboard)
        move = self.minmax.search(node, 4).content.pop()
        self.chessboard.push(move)

        # ATT Tabuleiro
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

        self.tbxLegalMoves.setText(self.convert_list_of_moves())
        self.txtMove.setText("")