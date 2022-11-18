import pygame
from obstacle import Obstacle
class Level:
    obstacle_list: list[Obstacle]
    obstacle_speed: int
    goal: pygame.Rect
    player_pos: tuple 

    def __init__(self, obstacle_list: list[Obstacle], obstacle_speed: int, goal: pygame.Rect, player_pos: tuple):
        self.obstacle_list = obstacle_list
        self.obstacle_speed = obstacle_speed
        self.goal = goal
        self.player_pos = player_pos