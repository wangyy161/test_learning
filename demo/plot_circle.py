import pygame
import sys
from pygame.locals import *
# pygame 初始化
pygame.init()
# 设置背景颜色和线条颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# 设置背景框大小
size = width, height = 600, 600
#position = width // 2, height // 2
# 设置帧率，返回clock 类
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("llls make")


while True:
    for event in pygame.event.get():
# 查找关闭窗口事件
        if event.type == QUIT:
            sys.exit()

# 填充背景色
    screen.fill(BLACK)


# 画一个圆和一个椭圆
    pygame.draw.ellipse(screen, GREEN, (100, 100, 400, 100), 1)
    pygame.draw.ellipse(screen, GREEN, (100, 100, 400, 400), 1)


# 刷新图
    pygame.display.flip()


    clock.tick(60)
