import pygame
from sys import exit
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

background_image_filename = '../image/curve_pattern.png'

background = pygame.image.load(background_image_filename).convert()
width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pts = []
knots = []
count = 0
screen.fill(WHITE)

clock = pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    pygame.draw.circle(screen, color, pt, thick)


def drawLine(pt0, pt1, color='GREEN', thick=3):
    drawPoint((100, 100), color, thick)
    drawPoint(pt0, color, thick)
    drawPoint(pt1, color, thick)




def drawPolylines(color='GREEN', thick=3):
    if (count < 2): return
    for i in range(count - 1):
        drawLine(pts[i], pts[i+1], color)
        pygame.draw.line(screen, color, pts[i], pts[i + 1], thick)


done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0

while not done:

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = [x, y]
    pygame.draw.circle(screen, RED, pt, 0)

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0:
        pts.append(pt)
        count += 1
        pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
        print("len:" + repr(len(pts)) + " mouse x:" + repr(x) + " y:" + repr(y) + " button:" + repr(
            button1) + " pressed:" + repr(pressed) + " add pts ...")
    else:
        print("len:" + repr(len(pts)) + " mouse x:" + repr(x) + " y:" + repr(y) + " button:" + repr(
            button1) + " pressed:" + repr(pressed))

    if len(pts) > 1:
        drawPolylines(GREEN, 1)

    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()
