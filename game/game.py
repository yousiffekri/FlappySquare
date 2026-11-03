

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
            

def UpperYchord(num):
    uyp = 0
    if num == 1:
        uyp = 200
    elif num == 2:
        uyp = 150
    elif num == 3:
        uyp = 100
    elif num == 4:
        uyp = 50
    
    return uyp
def lowerYchord(num):
    Ypos = 0
    if num == 1:
        Ypos = 300
    elif num == 2:
        Ypos = 250
    elif num == 3:
        Ypos = 200
    elif num == 4:
        Ypos = 150
    return Ypos





def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Square")
    running = True
    font = pygame.font.SysFont(None, 36)
    firstTube = pygame.Rect(700, 0, 60, 200)
    secondTube = pygame.Rect(700, 300, 60, 300)
    upper = [firstTube.copy()]
    lower = [secondTube.copy()]
    colided = False
    addedpoints = False
    readd = False
    velocitydown = 2
    tubevelocity = 2
    flapup = 40
    scorebox = pygame.Rect(0, 0, 120, 60)
    score = 0
    OScore = 0
# x, y, width, height
    flapper = pygame.Rect(100, 200, 10, 10)
    
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
        pygame.draw.rect(screen, RED, scorebox)

        ranum = random.randint(1, 4)

        flapper.y += velocitydown
        for tube in upper [:]:
            tube.x -= tubevelocity
            if tube.x < -60:
                upper.remove(tube)    
        if upper[-1].x <= 450:
            newTube = pygame.Rect(700,0,60,UpperYchord(ranum))
            upper.append(newTube)
        for tube in upper:
            pygame.draw.rect(screen, GREEN, tube)
        
        
        for tube in lower [:]:
            tube.x -= tubevelocity
            if tube.x < -60:
                lower.remove(tube)                  
        if lower[-1].x <= 450:
            newTube = pygame.Rect(700,lowerYchord(ranum),60,300)
            lower.append(newTube)                   
        for tube in lower:
            pygame.draw.rect(screen, GREEN, tube)

        
        surfrace = font.render(f"Score: {score}",True,WHITE)
        rect = surfrace.get_rect(center = scorebox.center)
        screen.blit(surfrace,rect)

        if flapper.y < 0:
           flapper.y += 5

        if (flapper.y + 30) > HEIGHT:
            flapper.y -= 5
        for tube in upper:
            if tube.x == 18: 
                    score += 1
                
        if score >= 20:
            tubevelocity = 4
        for tube in upper:
            if flapper.colliderect(tube):
                colided = True
        for tube in lower:
            if flapper.colliderect(tube):
                colided = True

        if colided:
            velocitydown = 0
            tubevelocity = 0
            flapup = 0      


            
            

        
                
           
            


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()





if __name__ =="__main__":
    startscreen()
