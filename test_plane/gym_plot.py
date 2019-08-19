'''
1、本实验使用的是固定的障碍物（柱体），障碍物有四个；
2、不管舰载放进去的顺序；
3、使用三角形代替飞机，控制飞机的位置以及角度（绘制的图形进行旋转）；
4、放大或者缩小使用pygame的接口。
'''
from math import pi, sin, cos, asin, acos, degrees
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
        self.image_data = []
        self.image_data_last = []
        self.score = 0
        self.reward = 0

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
        overrange = False
        rot_x = (point_x - point[0]) * cos(angle) + (point_y - point[1]) * sin(angle) + point[0]
        rot_y = (point_y - point[1]) * cos(angle) - (point_x - point[0]) * sin(angle) + point[1]
        if rot_x < 0 or rot_x > 1000 or rot_y < 0 or rot_y > 1000:
            overrange = True
        return int(rot_x), int(rot_y), overrange
    def pixel_value(self, point1, point2):
        if abs(point1[0] - point2[0]) > abs(point1[1] - point2[1]):
            k = (point2[1] - point1[1]) / (point2[0] - point1[0])
            b = point1[1] - k * point1[0]
            # 判断哪个点
            if point1[0] > point2[0]:
                # 获取x坐标
                x_list = list(range(point2[0], point1[0]+1, 1))
            else:
                x_list = list(range(point1[0], point2[0] + 1, 1))
            y_list = np.array(x_list) * k + b
        else:
            if abs(point2[0] - point1[0]) > 0:
                k = (point2[1] - point1[1]) / (point2[0] - point1[0])
                b = point1[1] - k * point1[0]
                if point1[1] > point2[1]:
                    y_list = list(range(point2[1], point1[1]+1, 1))
                else:
                    y_list = list(range(point1[1], point2[1] + 1, 1))
                x_list = (np.array(y_list) - b) / k
            else:
                y_list = list(range(point2[1], point1[1]+1, 1))
                x_list = np.ones((len(y_list))) * point1[0]
        return np.array(x_list).astype(np.int), np.array(y_list).astype(np.int)

    def judge_overlapping(self, img_data_last, img_data, point_list):
        # 将两幅图像进行灰度化处理
        zero_num = 0
        gray_last = cv.cvtColor(img_data_last, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
        gray_now = cv.cvtColor(img_data, cv.COLOR_RGB2GRAY)  # 把输入图像灰度化
        img_new = gray_now - gray_last
        [x1, y1, x2, y2, x3, y3] = point_list
        x_list_1, y_list_1 = self.pixel_value([x1, y1], [x2, y2])
        x_list_2, y_list_2 = self.pixel_value([x3, y3], [x2, y2])
        x_list_3, y_list_3 = self.pixel_value([x2, y2], [x3, y3])
        zero_list = img_new[[x1, x2, x3], [y1,y2, y3]]
        if_zero = np.any(zero_list == 0)
        if if_zero:
            overlapping = True
            print('三个顶点处为零')
        else:
            self.zero_num_1 = 0
            self.zero_num_2 = 0
            self.zero_num_3 = 0
            zero_list_1 = img_new[x_list_1, y_list_1]
            zero_list_2 = img_new[x_list_2, y_list_2]
            zero_list_3 = img_new[x_list_3, y_list_3]
            continue_zero_num = 0
            for i in range(len(zero_list_1)):
                if zero_list_1[i] == 0:
                    continue_zero_num += 1
                    if continue_zero_num > 5:
                        self.zero_num_1 = continue_zero_num
                else:
                    continue_zero_num = 0
            continue_zero_num = 0
            for i in range(len(zero_list_2)):
                if zero_list_2[i] == 0:
                    continue_zero_num += 1
                    if continue_zero_num > 5:
                        self.zero_num_2 = continue_zero_num
                else:
                    continue_zero_num = 0
            continue_zero_num = 0
            for i in range(len(zero_list_3)):
                if zero_list_3[i] == 0:
                    continue_zero_num += 1
                    if continue_zero_num > 5:
                        self.zero_num_3 = continue_zero_num
                else:
                    continue_zero_num = 0
            if self.zero_num_1 > 5 or self.zero_num_2 > 5 or self.zero_num_3 > 5:
                overlapping = True
                print('..............此时，飞机放置位置超出边界或者与其他飞机存在重叠............')
            else:
                overlapping = False

        return overlapping
    def get_state_img(self, point, angle, size, if_init):

        if if_init:
            self.image_data = self.init_plot()
            terminal = False
            self.reward += 0.0
        else:
            self.image_data_last = self.image_data
            [x, y] = point
            plane_size1 = size * 4 + 20
            plane_size2 = (size * 4 + 20) / 2

            plane_size_1 = size * 4 + 26
            plane_size_2 = (size * 4 + 26) / 2
            # 开始投放飞机：主要参数为：飞机的位置点、飞机的朝向、飞机的型号
            # 使用等腰三角形进行替代
            x1, y1, overrange_1 = self.Rotate(x, y - plane_size1, point, angle)
            x2, y2, overrange_2 = self.Rotate(x - plane_size2, y + plane_size2, point, angle)
            x3, y3, overrange_3 = self.Rotate(x + plane_size2, y + plane_size2, point, angle)

            x_1, y_1, _ = self.Rotate(x, y - plane_size_1, point, angle)
            x_2, y_2, _ = self.Rotate(x - plane_size_2, y + plane_size_2, point, angle)
            x_3, y_3, _ = self.Rotate(x + plane_size_2, y + plane_size_2, point, angle)


            point_list = [x1, y1, x2, y2, x3, y3]
            if overrange_1 or overrange_2 or overrange_3:
                terminal_range = True
                self.reward -= 1
                print('###################  超出区域！！！###############')
            else:
                terminal_range = False
            rect = ((x_1, y_1), (x_2, y_2), (x_3, y_3))
            # 画出旋转之后的三角形
            pygame.draw.polygon(DISPLAYSURF, WHITE, rect)

            # pygame.display.update()
            pygame.display.flip()
            self.image_data = pygame.surfarray.array3d(pygame.display.get_surface())
            # cv.imshow('input_image', self.image_data)
            overlapping = self.judge_overlapping(self.image_data_last, self.image_data, point_list)
            if overlapping:
                terminal_lapping = True
                print('###################  出现重叠！！！###############3')
                self.reward -= 10
            else:
                terminal_lapping = False
                self.reward += 1
                print('此时放进去一个', size, '型飞机', '旋转角度为：', degrees(angle))
            if terminal_range or terminal_lapping:
                terminal = True
            else:
                terminal = False
        return self.image_data, terminal, self.reward









