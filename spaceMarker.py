import pygame

relogio = pygame.time.Clock()
fundo = pygame.image.load('assets/fundo.png')
icon = pygame.image.load('assets/icon.png')
tamanho = (800,677)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Space Marker')
pygame.display.set_icon(icon)
#pygame.mixer.music.load('assets/som.mp3')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    tela.blit(fundo,(0,0))

    pygame.display.update()
    relogio.tick(60)
    