import pygame
import math
WIDTH = 600
HEIGHT = 600
def update():
   pass
def draw():
   screen.fill((0, 0, 0))
   def draw_mouse(x,y):
       screen.draw.text('x: ' + str(x)+ '\n' + 'y: ' + str(y),(0, 0))
       screen.draw.filled_circle((x, y), 10, color=(255, 0, 0))
   mouse_x, mouse_y = pygame.mouse.get_pos()
   draw_mouse(mouse_x, mouse_y)