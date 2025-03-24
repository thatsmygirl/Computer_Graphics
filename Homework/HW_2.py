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

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pts = []
knots = []
count = 0
# screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt)
    pygame.draw.circle(screen, color, pt, thick)


# HW2 implement drawLine with drawPoint
def drawLine(pt0, pt1, color='GREEN', thick=3):

    x0, y0 = pt0
    x1, y1 = pt1

    for x in range(x0, x1 + 1):
        y = round((y1 - y0) / (x1 - x0) * (x - x0) + y0)
        drawPoint((x, y), color, thick)


def coordinateFreeDrawLine(pt0, pt1, color='GREEN', thick=3):

    x0, y0 = pt0
    x1, y1 = pt1

    steps = max(abs(x1 - x0), abs(y1 - y0))

    for i in range(steps + 1):
        t = i / steps  # 보간 파라미터 (0 ~ 1)
        x = round((1 - t) * x0 + t * x1)  # Coordinate-free 보간 적용
        y = round((1 - t) * y0 + t * y1)
        drawPoint((x, y), color, thick)



def drawPolylines(color='GREEN', thick=3):
    if (count < 2): return
    for i in range(count - 1):
        drawLine(pts[i], pts[i + 1], color, thick) # HW_2 Linear
        # coordinateFreeDrawLine(pts[i], pts[i + 1], color, thick) # HW_2 Coordinate Free Linear


# Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
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
        # drawLagrangePolylines(BLUE, 10, 3)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()
