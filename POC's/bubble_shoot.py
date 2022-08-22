import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done = False
while done==False:
    for itm in pygame.event.get():
        if itm.type == pygame.QUIT:
            print('success')
            done = True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
    pygame.display.flip()
