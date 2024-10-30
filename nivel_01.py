import pygame

# Inicializar o Pygame
pygame.init()

# Definir dimensões da tela
TELA_LARGURA = 800
TELA_ALTURA = int(TELA_LARGURA * 0.8)

# Configurar a tela do jogo
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Jogo em Pygame')

# Definir a classe Soldado
class Soldado(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        img = pygame.image.load('img/jogador/jogador/jogador_Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Instanciar o soldado
x = 200
y = 200
scale = 3
jogador = Soldado(x, y, scale)

# Loop principal do jogo
run = True
while run:
    # Preencher o fundo com uma cor, por exemplo, preto
    tela.fill((0, 0, 0))
    # Desenhar o jogador na tela
    tela.blit(jogador.image, jogador.rect)

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Atualizar a tela
    pygame.display.update()

# Sair do Pygame
pygame.quit()
