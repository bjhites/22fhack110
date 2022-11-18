import pygame
class Obstacle:
    obstacle_move: int  = 1
    obstacle_rect: pygame.Rect

    def __init__(self, rect: pygame.Rect):
        self.obstacle_rect = rect