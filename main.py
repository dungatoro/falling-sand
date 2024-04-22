from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import threading

SAND = (255, 255, 0, 255)
AIR  = (0,   0,   0, 255)

WIDTH, HEIGHT = 300, 300
RAD = 5

FRAMERATE = 60

def apply_gravity(surface,pixels,startx,endx):
    for y in range(HEIGHT-2, -1, -1): # start at one from the bottom
        x = startx 
        while x < endx:
            if pixels[x,y] == surface.map_rgb(SAND):
                if pixels[x,y+1] == surface.map_rgb(AIR): # drop down if theres space
                    pixels[x,y+1] = surface.map_rgb(SAND) 
                    pixels[x,y] = surface.map_rgb(AIR) 
                elif x > 0 and pixels[x-1,y+1] == surface.map_rgb(AIR): # drop down-right if theres space
                    pixels[x-1,y+1] = surface.map_rgb(SAND)
                    pixels[x,y] = surface.map_rgb(AIR)
                elif x < WIDTH-1 and pixels[x+1, y+1] == surface.map_rgb(AIR): # drop down-left if theres space
                    pixels[x+1,y+1] = surface.map_rgb(SAND)
                    pixels[x,y] = surface.map_rgb(AIR)
            x += 1

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
    pxarrray = pygame.PixelArray(surface)


    t1 = threading.Thread(target=apply_gravity, args=(surface, pxarrray,0,101))
    t2 = threading.Thread(target=apply_gravity, args=(surface, pxarrray,101,201))
    t3 = threading.Thread(target=apply_gravity, args=(surface, pxarrray,201,299))
    t1.start()
    t3.start()
    t1.join()
    t3.join()
    t2.start()
    t2.join()
    del pxarrray
    screen.blit(surface, (0,0))
    pygame.display.flip()

    clock.tick(FRAMERATE)
    print(clock.get_fps())