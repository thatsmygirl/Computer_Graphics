import pygame
from sys import exit
import numpy as np

width, height = 800, 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Cubic Hermite Interpolation")

WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

pts = []
clock = pygame.time.Clock()
margin = 6

def compute_tangents(points):
    """각 점에서의 접선(derivative) 벡터를 중앙차분/전진·후진차분으로 계산"""
    n = len(points)
    tangents = []
    for i in range(n):
        if i == 0:
            dx = points[1][0] - points[0][0]
            dy = points[1][1] - points[0][1]
        elif i == n - 1:
            dx = points[i][0] - points[i - 1][0]
            dy = points[i][1] - points[i - 1][1]
        else:
            dx = (points[i + 1][0] - points[i - 1][0]) / 2.0
            dy = (points[i + 1][1] - points[i - 1][1]) / 2.0
        tangents.append((dx, dy))
    return tangents

def draw_hermite_curve(color=BLUE, samples=100, thick=2):
    """Cubic Hermite 보간곡선"""
    n = len(pts)
    if n < 2:
        return

    tangents = compute_tangents(pts)
    curve = []
    # 각 구간별로 t ∈ [0,1] 에 대해 보간
    for i in range(n - 1):
        p0 = np.array(pts[i], dtype=float)
        p1 = np.array(pts[i + 1], dtype=float)
        m0 = np.array(tangents[i], dtype=float)
        m1 = np.array(tangents[i + 1], dtype=float)

        for t in np.linspace(0, 1, samples):
            h00 =  2*t**3 - 3*t**2 + 1
            h10 =      t**3 - 2*t**2 + t
            h01 = -2*t**3 + 3*t**2
            h11 =      t**3 -     t**2

            point = h00 * p0 + h10 * m0 + h01 * p1 + h11 * m1
            curve.append((int(point[0]), int(point[1])))

    pygame.draw.lines(screen, color, False, curve, thick)

pressed = old_pressed = 0
old_button1 = 0
done = False

while not done:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, _, _ = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0:
        pts.append((x, y))

    old_button1 = button1
    old_pressed = pressed

    for p in pts:
        pygame.draw.circle(screen, RED, p, 4)

    if len(pts) > 1:
        draw_hermite_curve(BLUE, samples=200, thick=2)

    pygame.display.update()

pygame.quit()
