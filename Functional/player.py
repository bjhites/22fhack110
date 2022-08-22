import pygame

class Player:
    num: int = 0
    speed: int = 4
    moving_up: int = 0
    moving_down: int = 0
    moving_left: int = 0
    moving_right: int = 0
    rect: pygame.Rect
    score: int = 0

    def __init__(self, num: int, rect: pygame.Rect):
        self.num = num
        self.rect = rect

    def move(self) -> None:
        speed = 4
        if((self.moving_up == 1 or self.moving_down == 1) and (self.moving_right == 1 or self.moving_left == 1)):
            speed = 2
        if(self.moving_up == 1):
            self.rect.y -= speed
        if(self.moving_down == 1):
            self.rect.y += speed
        if(self.moving_left == 1):
            self.rect.x -= speed
        if(self.moving_right == 1):
            self.rect.x += speed

    def getKeyDown(self, key: pygame.event.Event) -> None:
        if key.key == pygame.K_w:
            self.setMovingUp(1)
        if key.key == pygame.K_s:
            self.setMovingDown(1)
        if key.key == pygame.K_a:
            self.setMovingLeft(1)
        if key.key == pygame.K_d:
            self.setMovingRight(1)
        
    def getKeyUp(self, key: pygame.event.Event) -> None:
        if key.key == pygame.K_a:
            self.setMovingLeft(0)
        if key.key == pygame.K_d:
            self.setMovingRight(0)
        if key.key == pygame.K_w:
            self.setMovingUp(0)
        if key.key == pygame.K_s:
            self.setMovingDown(0)

    def getMovingUp(self) -> int:
        return self.moving_up
    
    def setMovingUp(self, x: int) -> None:
        self.moving_up = x

    def setMovingLeft(self, x: int) -> None:
        self.moving_left = x

    def setMovingRight(self, x: int) -> None:
        self.moving_right = x
    
    def getMovingDown(self) -> int:
        return self.moving_down
    
    def setMovingDown(self, x: int) -> None:
        self.moving_down = x

    def getRect(self) -> pygame.Rect:
        return self.rect

    def getScore(self) -> int:
        return self.score