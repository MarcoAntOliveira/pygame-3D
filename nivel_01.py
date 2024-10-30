import pygame

pygame.init()


TELA_LARGURA = 800
TELA_ALTURA = int(TELA_LARGURA* 0.8)

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('jogo em pygame')

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()


