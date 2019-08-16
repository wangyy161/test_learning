from pygame.locals import *
import cv2
import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

HALF_WINDOW_WIDTH = int(WINDOW_WIDTH / 2)
HALF_WINDOW_HEIGHT = int(WINDOW_HEIGHT / 2)

BASIC_FONT = pygame.font.Font('freesansbold.ttf', 12)
DISPLAYSURF = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

WHITE        = (255, 255, 255)
BLACK		 = (  0,   0,   0)
RED 		 = (200,  72,  72)
LIGHT_ORANGE = (198, 108,  58)
ORANGE       = (180, 122,  48)
GREEN		 = ( 72, 160,  72)
BLUE 		 = ( 66,  72, 200)
YELLOW 		 = (162, 162,  42)
NAVY         = ( 75,   0, 130)
PURPLE       = (143,   0, 255)

class Pygame_plot():
    def __init__(self):

    def main(self):




if __name__ == '__main__':
    plot = Pygame_plot()
    plot.main()