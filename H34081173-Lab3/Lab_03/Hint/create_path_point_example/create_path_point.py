import pygame

pygame.init()
win = pygame.display.set_mode((1024, 600))
clock = pygame.time.Clock()
points = []
# coordinate of the rect surface
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            points.append((x, y))

    # draw window
    win.fill((0, 0, 0))
    background_image = pygame.transform.scale(pygame.image.load("../../lab_03_tmp/images/Map.png"), (1024,600))
    background_posX=0
    background_posY=0
    win.blit(background_image, (background_posX, background_posY))
    # draw point
    for p in points:
        pygame.draw.circle(win, (255, 0, 0), p, 5)
    pygame.display.update()
pygame.quit()

with open('path_point.txt', 'w') as f:
    f.write(f"{points}")
