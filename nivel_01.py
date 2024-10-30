import pygame
from pygame.sprite import _Group

pygame.init()


TELA_LARGURA = 800
TELA_ALTURA = int(TELA_LARGURA* 0.8)

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('jogo em pygame')
class Soldado(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/jogador/jogador/jogador_Idle/0.png')
        self.image = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))

        self.rect = img.get_rect()
        self.rect.center = (x, y)

x = 200
y = 200
scale = 3




run=True
while run:
    tela.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()        
pygame.quit()


