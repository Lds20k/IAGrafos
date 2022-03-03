import random
import math
import copy

class TicTacToe:
    def __init__(self):
        self.state: list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.turn: str = 'X' # sempre começa com o x
        self.draw: bool = False
    
    def copy_state(self):
        return copy(self.state)

    def __str__(self):
        board = ""
        for i in range(0,3):
            board += f"{self.state[0+(i*3)]} | {self.state[1+(i*3)]} | {self.state[2+(i*3)]}\n"

        return board
    
    def __toggle_turn__(self):
        if self.turn == "O":
            self.turn = "X"
        else:
            self.turn = "O"

    def move(self, position):
        self.state[position] = self.turn
        self.__toggle_turn__()
    
    def successor(self):
        next_states = []
        for index in range(9):
            if self.state[index] == " ":
                next_states.append(tuple([index, self.turn]))
        return next_states

    def is_end(self):
        e = self.state
        return \
            e[0] == e[1] and e[0] == e[2] and e[0] != " " or \
            e[3] == e[4] and e[3] == e[5] and e[3] != " " or \
            e[6] == e[7] and e[6] == e[8] and e[6] != " " or \
            e[0] == e[3] and e[0] == e[6] and e[0] != " " or \
            e[1] == e[4] and e[1] == e[7] and e[1] != " " or \
            e[2] == e[5] and e[2] == e[8] and e[2] != " " or \
            e[0] == e[4] and e[0] == e[8] and e[0] != " " or \
            e[2] == e[4] and e[2] == e[6] and e[2] != " "

    def is_draw(self):
        if self.draw:
            return self.draw
        for state in self.state:
           if state == " ": 
               return False
        return True
    
    def utility(self):
        pass

def minimax(state, action, turn, agent_symbol):
    state.move(action, turn)
    if state.is_end():
        return state.utility(agent_symbol)
    # max
    util = -1000
    for edge in state.successor():
        symbol = action = edge[0]
        
        state_copy = state.copy_state()
        util = math.max(util, minimax(state_copy, action, state.turn,symbol))


game = TicTacToe()
#print(game.successor())

while(not game.is_end() and not game.is_draw()):
    action = random.choice(game.successor())
    game.move(action[0])

print(game)

minimax(game.state, game.move(). game.turn)