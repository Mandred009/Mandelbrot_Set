import random

import pygame

pygame.init()

window_width = 1000;
window_height = 700;
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mandelbrot Set")
display_surface.fill((100,100,10))

fps = 60
clock = pygame.time.Clock()

# pygame.draw.circle(display_surface, (255,255,255),(500,350) ,1)

def pallete_selection(number,max):
    #print(number)
    return (max-number)

for x0 in range(0, 1000):
    for y0 in range(0, 700):
        x, y = 0,0
        iteration = 0
        max_iteration = 255
        while ((x * x) + (y * y) <= 4 and iteration < max_iteration):
            temp = (x * x) - (y * y) + ((x0-500)/200)
            y = (2 * x * y )+ ((350-y0)/200)
            x = temp
            iteration+=1
        col=pallete_selection(iteration,max_iteration)
        pygame.draw.circle(display_surface, (col,col,col) , (x0, y0), 1)

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
