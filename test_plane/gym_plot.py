'''
1、本实验使用的是固定的障碍物（柱体），障碍物有四个；
2、不管舰载放进去的顺序；
3、使用三角形代替飞机，控制飞机的位置以及角度（绘制的图形进行旋转）；
4、放大或者缩小使用pygame的接口。
'''
from math import pi, sin, cos, asin, acos
import pygame
pygame.init()
import random

WINDOW_WIDTH = 1000
WINDOW_HIGHT = 1000

HALF_WIDTH = WINDOW_WIDTH / 2
HALF_HIGHT = WINDOW_HIGHT / 2

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

class Pendulum:
    def __init__(self):
        global FPS_CLOCK, DISPLAYSURF, BASIC_FONT
        FPS_CLOCK = pygame.time.Clock()
        pygame.display.set_caption('Plane_board')

        self.init = True
        self.score = 0
        self.reward = 0
        self.direction = ''
        self.TargetPosition_First = 0
        self.TargetPosition_Gauss_First = 0

    def get_state_img(self, state):
        pygame.init()
        # pygame.display.set_caption('Pendulum')
        DISPLAYSURF.fill(BLACK)
        x_1 = random.randint(10, 20)




        thetacos = acos(state[0])
        thetasin = asin(state[1])

        # 由于asin的取值范围为：-pi/2 ~ pi/2，cos取值范围为：0 ~ pi
        if thetasin >= 0:
            theta = -thetacos
        else:
            theta = thetacos
        # print('.....gym_plot.....', theta, '.....gym_plot.....')
        theta = (theta / pi) * 180
        # print('.....gym_plot.....', theta, '.....gym_plot.....')
        Horizontal_start = [100, int(WINDOW_HIGHT / 2)]
        Horizontal_end   = [380, int(WINDOW_HIGHT / 2)]
        center = [int(WINDOW_WIDTH / 2), int(WINDOW_HIGHT / 2)]
        radius = 140
        Vertical_start = [int(WINDOW_WIDTH / 2), 50]

        angle = theta - 90

        # 通过半径、角度、圆点坐标求解直线上的点
        x1 = center[0] + radius * cos(angle * pi / 180)
        x2 = center[1] + radius * sin(angle * pi / 180)
        Pendulum_Point = (x1, x2)
        # 将扭矩作为输入信息，进行可视化，但是好像还是没有什么效果
        radius = abs(int(state[2] * 10))
        # 这段是防止禅城半径为0的信息，会报错，所以进行处理一下下
        if radius <= 5:
            radius = 5
        Rect = ((int(WINDOW_WIDTH / 2) - radius, int(WINDOW_HIGHT / 2) - radius), (radius * 2, radius * 2))
        # print('..........', Rect, '..........')
        pygame.draw.line(DISPLAYSURF, WHITE, Horizontal_start, Horizontal_end, 8)
        pygame.draw.line(DISPLAYSURF, ORANGE, Vertical_start, center, 10)
        pygame.draw.line(DISPLAYSURF, GREEN, Pendulum_Point, center, 8)
        if state[2] >= 0:
            pygame.draw.ellipse(DISPLAYSURF, NAVY, Rect, 4)
        else:
            pygame.draw.ellipse(DISPLAYSURF, YELLOW, Rect, 4)
        pygame.display.update()
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())

        return image_data








