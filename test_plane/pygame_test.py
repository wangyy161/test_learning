import pygame,sys
import time
import random
import cv2 as cv

pygame.init()
screencaption=pygame.display.set_caption('hello world')
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
zhijing=random.randint(0,100)
width=random.randint(0,255)
height=random.randint(0,100)
top=random.randint(0,400)
left=random.randint(0,500)
pygame.draw.circle(screen,[0,0,0],[top,left],zhijing,1)
pygame.draw.rect(screen,[255,0,0],[left,top,width,height],3)
# pygame.gfxdraw.filled_trigon(screen, 10, 10, 5, 15, 10, 20, 0)
# pygame.gfxdraw.aacircle(screen, 10, 10, 30, [0,255,255])
x = 100
y = 100
# pygame.draw.rect(screen,(255,171,244),(x,y-180,200,180))
# #brown door
# pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
# #yellow door knob
# pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
#triangle roof
pygame.draw.polygon(screen, (125, 125, 125), ( (x,y-20),(x-10,y+10),(x+10,y+10) ) )
pygame.display.flip()
image_data = pygame.surfarray.array3d(pygame.display.get_surface())

# pygame.transform.rotate(Surface, angle) (旋转)
# draw_window(x+20,y-90)
# draw_window(x+130,y-90)
cv.imshow('input_image', image_data)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()