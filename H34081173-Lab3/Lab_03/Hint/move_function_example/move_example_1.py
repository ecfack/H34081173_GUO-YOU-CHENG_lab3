import pygame

pygame.init()
win = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()

# coordinate of the rect surface
x = 0
y = 100

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update the coordinate each frame
    x += 2
    y += 1

    # draw
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), [x, y, 50, 50])
    pygame.display.update()
pygame.quit()
