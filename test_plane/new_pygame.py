from math import pi, sin, cos, asin, acos, degrees
import pygame
import cv2 as cv
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HIGHT = 1000

HALF_WIDTH = WINDOW_WIDTH / 2
HALF_HIGHT = WINDOW_HIGHT / 2

pygame.init()
BASIC_FONT = pygame.font.Font('freesansbold.ttf', 8)
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))

WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
RED          = (200,  72,  72)
LIGHT_ORANGE = (198, 108,  58)
ORANGE       = (180, 122,  48)
GREEN        = ( 72, 160,  72)
YELLOW       = (162, 162,  46)
NAVY         = ( 75,   0, 255)
PURPLE       = (143,   0, 255)

class Plane_plot_now:
    def __init__(self):
        global FPS_CLOCK, DISPLAYSURF, BASIC_FONT
        FPS_CLOCK = pygame.time.Clock()
        pygame.display.set_caption('Plane_board_now')

    # 此处的point表示的是三角形的中心点，size表示的是三角形的大小（0，1，2）表示三种类型，还有一个
    # 是障碍物的位置，使用四个区域的中心点坐标进行控制
    def plot_now(self, rect):
        pygame.draw.polygon(DISPLAYSURF, WHITE, rect)
        pygame.display.update()
        pygame.display.flip()
        image_data_now = pygame.surfarray.array3d(pygame.display.get_surface())
        return image_data_now
    cv.imshow('123', image_data_now)