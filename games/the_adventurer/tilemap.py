from json.encoder import INFINITY

from pygame import Color


class TileMap:
    SOIL = 1
    WATER = 2
    QUICKSAND = 3
    OBSTACLE = 4

    tiles = {
        str(Color(127, 51, 0)): SOIL,
        str(Color(0, 148, 255)): WATER,
        str(Color(255, 216, 0)): QUICKSAND,
        str(Color(0, 0, 0)): OBSTACLE
    }

    weights = {
        SOIL: 1,
        WATER: 3,
        QUICKSAND: 6,
        OBSTACLE: INFINITY
    }

    def __init__(self, list_map, size_x, size_y):
        self.list_map = list_map
        self.size_x = size_x
        self.size_y = size_y
    
    def get_weight(self, x, y):
        return self.list_map[x + (self.size_y * y)][1]
