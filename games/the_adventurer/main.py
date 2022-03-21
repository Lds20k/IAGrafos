import logging
import math
import os

import pygame
from games.the_adventurer.player import Player
from games.the_adventurer.tilemap import TileMap
from pygame import Color, Surface, image
from search.astar import AStarSearch
from struture.node import Node

current_path = os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger(__name__)

SCALE = 25

class TheAdventurer:
    
    def __init__(self, tilemap_path: str, goal:list):
        self.tilemap = self.__load_tilemap__(tilemap_path)
        self.player = Player("Josenildo", 0, 0, self.tilemap)
        self.goal = goal

    def __load_tilemap__(self, tilemap_path):
        path = f"{current_path}\images\{tilemap_path}"
        logger.info(f"Load bmp image: {path}")
        tilemap_image: Surface = image.load_basic(path)

        image_size = tilemap_image.get_size()
        logger.info(f"Image size: {image_size}")

        tilemap = []
        for y in range(image_size[1]):
            for x in range(image_size[0]):
                color = Color(tilemap_image.get_at((x, y)))
                tile = TileMap.tiles[str(color)]
                weight = TileMap.weights[tile]
                tilemap.append(tuple([tile, weight]))
        
        logger.info(f"Load map: {tilemap}")
        return TileMap(tilemap, image_size[0], image_size[1])
    
    def reached_goal(self, node: Node):
        player: Player = node.content
        return player.pos_x == self.goal[0] and player.pos_y == self.goal[1]

    def euclidean_heuristic(self, node: Node):
        player: Player = node.content
        px = math.pow(player.pos_x - self.goal[0], 2)
        py = math.pow(player.pos_y - self.goal[1], 2)
        return math.sqrt(px + py)
    
    def manhattan_heuristic(self, node: Node):
        player: Player = node.content
        px = abs(player.pos_x - self.goal[0])
        py = abs(player.pos_y - self.goal[1])
        return px + py

def start():
    logger.info("Game is started!")

    print("\nMapas:")
    for root, dirs, files in os.walk(f"{current_path}\images", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    
    image_path = input("Digite o nome do mapa, sem a extensão, que esta na pasta imagem: ")
    if image_path == "":
        image_path = "example_map"
    image_path = f"{image_path}.bmp"

    game = TheAdventurer(image_path, [7, 7])

    size_x = game.tilemap.size_x * SCALE
    size_y = game.tilemap.size_y * SCALE

    display_surface = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption('A*')

    image = pygame.image.load(f"{current_path}\images\{image_path}")
    image = pygame.transform.scale(image, (size_x, size_y))

    euc_color = Color(0, 255, 0)
    man_color = Color(0, 0, 255)

    path_euc = None
    path_man = None

    euc_search = AStarSearch(game.reached_goal, game.player.generate_moves, game.euclidean_heuristic)
    man_search = AStarSearch(game.reached_goal, game.player.generate_moves, game.manhattan_heuristic)
    
    run = True
    run_alg = False
    while run:
        display_surface.fill(Color(0, 0, 0))
        display_surface.blit(image, (0, 0))

        if run_alg:
            path_euc = euc_search.search(Node(game.player))
            logger.info(f"Generated euclidean heuristic path = {path_euc}")
            
            path_man = man_search.search(Node(game.player))
            logger.info(f"Generated manhattan heuristic path = {path_man}")
            
            run_alg = False

        draw_path(display_surface, euc_color, 6, path_euc)
        draw_path(display_surface, man_color, 3, path_man)

        draw_circle(display_surface, path_euc)
        draw_circle(display_surface, path_man)
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x = math.floor(x / SCALE)
                    y = math.floor(y / SCALE)
                    game.goal = [x, y]
                    run_alg = True

                pygame.display.flip()
                pygame.display.update()


def draw_path(screen: Surface, color: Color, width: int, node: Node):
    if node is None:
        return
    
    node_it = node
    while node_it.edge_ant is not None:
        node_ant = node_it
        node_it = node_it.edge_ant.node_ant
        pygame.draw.line(screen, Color(0,0,0), (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), (node_ant.content.pos_x * SCALE + SCALE/2, node_ant.content.pos_y * SCALE + SCALE/2), width=width+1)
        pygame.draw.line(screen, color, (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), (node_ant.content.pos_x * SCALE + SCALE/2, node_ant.content.pos_y * SCALE + SCALE/2), width=width)

def draw_circle(screen: Surface, node: Node):
    if node is None:
        return
    
    node_it = node
    while node_it.edge_ant is not None:
        pygame.draw.circle(screen, Color(0,0,0), (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), 6)
        pygame.draw.circle(screen, Color(255,255,255), (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), 5)
        node_it = node_it.edge_ant.node_ant
    
    pygame.draw.circle(screen, Color(0,0,0), (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), 6)
    pygame.draw.circle(screen, Color(255,255,255), (node_it.content.pos_x * SCALE + SCALE/2, node_it.content.pos_y * SCALE + SCALE/2), 5)
        

        