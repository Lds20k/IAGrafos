from games.the_adventurer.tilemap import TileMap
from struture.node import Edge, Node


class Player:

    def __init__(self, name: str, pos_x: int, pos_y: int, tilemap: TileMap):
        self.name: str = name
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.tilemap: TileMap = tilemap
    
    def __create_player__(self, x, y):
        return Player(self.name, self.pos_x + x, self.pos_y + y, self.tilemap)

    def generate_moves(self, node: Node, calculate_heuristic):
        player: Player = node.content
        moves = []

        # CIMA
        y = player.pos_y - 1
        if(y >= 0):
            new_player: Player = player.__create_player__(0, -1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))

        # BAIXO
        y = player.pos_y + 1
        if(y < self.tilemap.size_y):
            new_player: Player = player.__create_player__(0, 1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        # ESQUERDA
        x = player.pos_x - 1
        if(x >= 0):
            new_player: Player = player.__create_player__(-1, 0)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        # DIREITA
        x = player.pos_x + 1
        if(x < self.tilemap.size_x):
            new_player: Player = player.__create_player__(1, 0)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))

        # CIMA-DIREITA
        x = player.pos_x + 1
        y = player.pos_y - 1
        if(y >= 0 and x < self.tilemap.size_x):
            new_player: Player = player.__create_player__(1, -1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        # CIMA-ESQUERDA
        x = player.pos_x - 1
        y = player.pos_y - 1
        if(y >= 0 and x >= 0):
            new_player: Player = player.__create_player__(-1, -1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        # BAIXO-DIREITA
        x = player.pos_x + 1
        y = player.pos_y + 1
        if(y < self.tilemap.size_y and x < self.tilemap.size_x):
            new_player: Player = player.__create_player__(1, 1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        # BAIXO-ESQUERDA
        x = player.pos_x - 1
        y = player.pos_y + 1
        if(y < self.tilemap.size_y and x >= 0):
            new_player: Player = player.__create_player__(-1, 1)
            node = Node(new_player)
            weight = self.tilemap.get_weight(new_player.pos_x, new_player.pos_y) + calculate_heuristic(node)
            moves.append(Edge(node, weight))
        
        return moves

    def __str__(self) -> str:
        return f"({self.pos_x}, {self.pos_y})"
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Player):
            return NotImplemented

        return self.pos_x == __o.pos_x and self.pos_y == __o.pos_y

