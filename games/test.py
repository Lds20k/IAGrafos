import chess

# Iniciao tabuleiro
board = chess.Board()

# Preto é false
# Branco é true
print("PRETO:", chess.BLACK)
print("BRANCO:", chess.WHITE)

# Printa o turno
print("TURNO:", board.turn)

# Printa o tabuleiro
print(board)

# Pega a peça da casa
# De baixo pra cima, as brancas são as maiuscula
print("PEÇA:",board.piece_at(0))

# Pega a cor da peça
print("COR DA PEÇA:", board.piece_at(0).color)

# Retorna a cor do turno
turn_color = lambda turn: "Branco\0" if turn else "Preto\0"
print(turn_color(board.turn))

# Retorna se o jogo terminou
print("JOGO TERMINOU:", board.is_game_over())
print("JOGO TERMINOU:", board.outcome())

# Função sucessora def
print(board.legal_moves)
test = board.copy()
test.push_san("a4")
print("TESTE:")
print(test)
print()
print("BOARD:")
print(board)
print()

print(test.legal_moves)

