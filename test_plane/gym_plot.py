'''
1、本实验使用的是固定的障碍物（柱体），障碍物有四个；
2、不管舰载放进去的顺序；
3、使用三角形代替飞机，控制飞机的位置以及角度（绘制的图形进行旋转）；
4、放大或者缩小使用pygame的接口。
'''
from math import pi, sin, cos, asin, acos
import pygame
import cv2 as cv
import numpy as np

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

class Plane_plot:
    def __init__(self):
        global FPS_CLOCK, DISPLAYSURF, BASIC_FONT
        FPS_CLOCK = pygame.time.Clock()
        pygame.display.set_caption('Plane_board')
        # 该部分计算障碍物的坐标
        self.obstacle = {}
        self.obstacle_num = 1
        self.obstacle_x = [int(WINDOW_WIDTH / 3), int(2 * WINDOW_WIDTH / 3)]
        self.obstacle_y = [int(WINDOW_HIGHT / 3), int(2 * WINDOW_HIGHT / 3)]
        for i in range(len(self.obstacle_x)):
            for j in range(len(self.obstacle_y)):
                self.obstacle[self.obstacle_num] = [self.obstacle_x[i], self.obstacle_y[j]]
                self.obstacle_num += 1

        self.init = True
        self.score = 0
        self.reward = 0
        self.direction = ''
        self.TargetPosition_First = 0
        self.TargetPosition_Gauss_First = 0

        self.obstacle_size = 20

    # 此处的point表示的是三角形的中心点，size表示的是三角形的大小（0，1，2）表示三种类型，还有一个
    # 是障碍物的位置，使用四个区域的中心点坐标进行控制
    def init_plot(self):

        pygame.init()
        # pygame.display.set_caption('Pendulum')
        DISPLAYSURF.fill(BLACK)
        # 障碍物绘制
        for i in range(self.obstacle_num - 1):
            x, y = self.obstacle[i+1][0], self.obstacle[i+1][1]
            obstacle_rect = pygame.Rect(x + self.obstacle_size / 2, y + self.obstacle_size / 2, self.obstacle_size, self.obstacle_size)
            pygame.draw.rect(DISPLAYSURF, WHITE, obstacle_rect)
        pygame.display.flip()
        # pygame.display.update()
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        # cv.imshow('hello', image_data)
        return image_data

    def Rotate(self, point_x, point_y, point, angle):
        rot_x = (point_x - point[0]) * cos(angle) + (point_y - point[1]) * sin(angle) + point[0]
        rot_y = (point_y - point[1]) * cos(angle) - (point_x - point[0]) * sin(angle) + point[1]
        return int(rot_x), int(rot_y)
    def judge_overlapping(self, imge_data, rect):
        pygame.init()
        screencaption = pygame.display.set_caption('hello world')
        screen = pygame.display.set_mode([1000,1000])
        screen.fill(BLACK)
        pygame.draw.polygon(DISPLAYSURF, WHITE, rect)
        # pygame.display.update()
        pygame.display.flip()
        image_data_now = pygame.surfarray.array3d(pygame.display.get_surface())

        gray_last = cv.cvtColor(imge_data, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
        gray_now = cv.cvtColor(image_data_now, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化

        value = np.dot(gray_last, gray_now)
        if value == 0:
            overlapping = True
        else:
            overlapping = False
        return overlapping
    def get_state_img(self, point, angle, size, if_init):

        if if_init:
            image_data = self.init_plot()
            terminal = False
        else:
            [x, y] = point
            plane_size_1 = size * 4 + 20
            plane_size_2 = (size * 4 + 20) / 2
            # 开始投放飞机：主要参数为：飞机的位置点、飞机的朝向、飞机的型号
            # 使用等腰三角形进行替代
            x1, y1 = self.Rotate(x, y - plane_size_1, point, angle)
            x2, y2 = self.Rotate(x - plane_size_2, y + plane_size_2, point, angle)
            x3, y3 = self.Rotate(x + plane_size_2, y + plane_size_2, point, angle)
            rect = ((x1, y1), (x2, y2), (x3, y3))
            # 画出旋转之后的三角形
            pygame.draw.polygon(DISPLAYSURF, WHITE, rect)

            # pygame.display.update()
            pygame.display.flip()
            image_data = pygame.surfarray.array3d(pygame.display.get_surface())

            # cv.imshow('input_image', image_data)
            terminal = False

            # overlapping = self.judge_overlapping(image_data, rect)
            # if overlapping:
            #     terminal = True
            # else:
            #     terminal = False

        return image_data, terminal








