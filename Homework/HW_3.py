import pygame
import numpy as np
from sys import exit

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Barycentric Centroid Only")

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

clock = pygame.time.Clock()
pts = []
running = True
while running:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            pos = ev.pos
            if len(pts) < 3:
                pts.append(pos)
            else:
                pts.pop(0)
                pts.append(pos)

    screen.fill(WHITE)

    for i, p in enumerate(pts):
        pygame.draw.circle(screen, BLUE, p, 6)
        label = pygame.font.SysFont(None, 24).render(["A","B","C"][i], True, BLACK)
        screen.blit(label, (p[0]+5, p[1]-5))

    if len(pts) == 3:
        A, B, C = np.array(pts[0], float), np.array(pts[1], float), np.array(pts[2], float)
        P = ((A + B + C) / 3.0).astype(int)

        pygame.draw.polygon(screen, BLACK, pts, 1)

        pygame.draw.circle(screen, RED, tuple(P), 6)
        coord_text = f"P = ({P[0]}, {P[1]})"
        info = pygame.font.SysFont(None, 24).render(coord_text, True, BLACK)
        screen.blit(info, (10, 10))

    pygame.display.flip()

pygame.quit()
exit()
