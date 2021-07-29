import pygame
import math

pygame.init()

win = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()

point_A = (50, 100)
point_B = (800, 400)
x, y = point_A  # initial coordinate
counter = 0  # define a counter to count the footstep


def move(p_A, p_B):
    global x, y, counter
    stride = 1
    ax, ay = p_A  # x, y position of point A
    bx, by = p_B
    distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
    max_count = int(distance_A_B / stride)  # total footsteps that needed from A to B

    if counter < max_count:
        unit_vector_x = (bx - ax) / distance_A_B
        unit_vector_y = (by - ay) / distance_A_B
        delta_x = unit_vector_x * stride
        delta_y = unit_vector_y * stride

        # update the coordinate and the counter
        x += delta_x
        y += delta_y
        counter += 1


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move(point_A, point_B)
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, 0), point_A, 5)
    pygame.draw.circle(win, (255, 0, 0), point_B, 5)
    # draw the moving object
    pygame.draw.rect(win, (0, 0, 0), [x, y, 50, 50])
    pygame.display.update()
pygame.quit()
