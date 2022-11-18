import sys, pygame
from obstacle import Obstacle
from level import Level
# screen size
size = width, height = 640, 480


# screen and clock objects
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball: pygame.Rect = pygame.Rect(width/2, height/2, 50, 50)


goal: pygame.Rect = pygame.Rect(width-50, height/2, 50, 50)

obstacle_1: Obstacle = Obstacle(pygame.Rect((3*width)/4, height/2 + 20, 30, 50))
obstacle_2: Obstacle = Obstacle(pygame.Rect((3*width)/4 - 50, height/2, 30, 50))
obstacle_3: Obstacle = Obstacle(pygame.Rect((3*width)/4 + 50, height/2 - 30, 30, 50))

obstacle_list : list[Obstacle] = [obstacle_1, obstacle_2, obstacle_3]

level_one: Level = Level(obstacle_list, 2, goal, (width/2, height/2))
level_two: Level = Level(obstacle_list, 8, goal, (25, height/2))
level_list: list[Level] = [level_one, level_two]
def main():  
    pygame.init()

    pygame.mouse.set_pos(width/2, height/2)
    pygame.mouse.set_visible(False)
    current_level = 0
    while 1:
        # Sets frame rate
        time_delta = clock.tick(60)

        for obstacle in level_list[current_level].obstacle_list:
            if obstacle.obstacle_rect.y > (height/2) + 100:
                obstacle.obstacle_move = -1 * level_list[current_level].obstacle_speed
            elif obstacle.obstacle_rect.y < (height/2) - 100:
                obstacle.obstacle_move = level_list[current_level].obstacle_speed
            
            obstacle.obstacle_rect.y += obstacle.obstacle_move

        ball.centerx, ball.centery = pygame.mouse.get_pos()

        # fill background with solid color 
        screen.fill((50,50,50))
        
        for obstacle in level_list[current_level].obstacle_list:
            pygame.draw.rect(screen, (255, 80, 80), obstacle.obstacle_rect)
        
        pygame.draw.circle(screen, (255, 80, 12), (ball.centerx, ball.centery), ball.width/2)

        pygame.draw.circle(screen, (255, 80, 255), (goal.centerx, goal.centery), goal.width/2)

        if level_list[current_level].goal.colliderect(ball):
            print("you won!")
            current_level += 1
            if current_level == len(level_list):
                sys.exit()
            else:
                pygame.mouse.set_pos(level_list[current_level].player_pos)

        for obstacle in level_list[current_level].obstacle_list:
            if ball.colliderect(obstacle.obstacle_rect):
                pygame.mouse.set_pos(level_list[current_level].player_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main()