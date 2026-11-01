import pygame
import random

from colours import *
highest_score = 0

pygame.init()
def startscreen():
    global highest_score
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Square start screen")
   
    
    startbut = pygame.Rect(225, 200, 150, 60)
    welcome_box = pygame.Rect(50, 100, 500, 100)
    font = pygame.font.SysFont(None, 36)
    rs_font = pygame.font.SysFont(None, 18)
    clock = pygame.time.Clock()

    running = True
    start_game = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
                    running = False

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, welcome_box)
        surfrace = font.render(f"Flappy Square: Highest score is {highest_score}",True,GREEN)
        rect = surfrace.get_rect(center = welcome_box.center)
        screen.blit(surfrace,rect)

        pygame.draw.rect(screen, GREEN, startbut)
        s_surfrace = rs_font.render("Press  Space to play",True,WHITE)
        s_rect = s_surfrace.get_rect(center = startbut.center)
        screen.blit(s_surfrace,s_rect)

        pygame.display.flip()
            
        clock.tick(60)

    if start_game:
            main()
    else:
        pygame.quit()
            


def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Square")
    running = True
    upperTube = []
    lowerTube = []
    colided = False
    addedpoints = False
    velocitydown = 2
    flapup = 50

    flapper = pygame.Rect(100, 200, 30, 30)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    flapper.y -= flapup

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, flapper)
        flapper.y += velocitydown


        if flapper.y < 0:
           flapper.y += 5

        if (flapper.y + 30) > HEIGHT:
            flapper.y -= 5
           
            


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()





if __name__ =="__main__":
    startscreen()
