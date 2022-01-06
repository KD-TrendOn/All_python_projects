import pygame
pygame.init()
sc = pygame.display.set_mode((600, 400), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption('Наша игра')
pygame.display.set_icon(pygame.image.load('peyzajh.bmp'))
clock = pygame.time.Clock()
FPS = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
