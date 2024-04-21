from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

SAND = (255, 255, 0, 255)
AIR  = (0,   0,   0, 255)

WIDTH, HEIGHT = 300, 300
RAD = 5

FRAMERATE = 60

def apply_gravity(surface):
    for y in range(HEIGHT-2, -1, -1): # start at one from the bottom
        for x in range(WIDTH):
            if surface.get_at((x,y)) == SAND:
                if surface.get_at((x, y+1)) == AIR: # drop down if theres space
                    surface.set_at((x, y+1), SAND) 
                    surface.set_at((x, y), AIR)

                elif x > 0 and surface.get_at((x-1, y+1)) == AIR: # drop down-right if theres space
                    surface.set_at((x-1, y+1), SAND)
                    surface.set_at((x, y), AIR)

                elif x < WIDTH-1 and surface.get_at((x+1, y+1)) == AIR: # drop down-left if theres space
                    surface.set_at((x+1, y+1), SAND)
                    surface.set_at((x, y), AIR)

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))
surface.fill(AIR)

screen = pygame.display.get_surface()
screen.blit(surface, (0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            
            pygame.draw.circle(surface, SAND, (x,y), RAD)

    apply_gravity(surface)

    screen.blit(surface, (0,0))
    pygame.display.flip()

    clock.tick(FRAMERATE)