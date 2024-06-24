import pygame
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
fundo = pygame.image.load('assets/fundo.png')
fundoMenu = pygame.image.load('assets/imagemMenu.jpg')
icon = pygame.image.load('assets/icon.png')
tamanho = (800,677)
tela = pygame.display.set_mode(tamanho)
fonte = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',15)
fonte_titulo = pygame.font.Font(None, 60)
fonte_opcoes = pygame.font.Font(None, 36)
pygame.display.set_caption('Space Marker')
pygame.display.set_icon(icon)
pygame.mixer.music.load('assets/som.mp3')
pygame.mixer.music.play(-1)
branco = (255,255,255)
preto = (0,0,0)

estrelas = {}

botao_iniciar = None
botao_configuracoes = None
botao_sair = None

def menu_inicial():
    global botao_iniciar, botao_configuracoes, botao_sair
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if botao_iniciar.collidepoint(pos_mouse):
                    rodando = False
                elif botao_configuracoes.collidepoint(pos_mouse):
                    configuracoes()
                elif botao_sair.collidepoint(pos_mouse):
                    pygame.quit()
                    quit()

        tela.blit(fundoMenu,(0,0))

        texto_titulo = fonte_titulo.render('SPACE MARKER', True, branco)
        titulo_rect = texto_titulo.get_rect(center=(tela.get_width() // 2, 100))
        tela.blit(texto_titulo, titulo_rect)

        largura_opcao = 200
        altura_opcao = 50
        espacamento = 20
        margem_inferior = 50

        x = (tela.get_width() - (largura_opcao * 3 + espacamento * 2)) // 2
        y = tela.get_height() - margem_inferior - altura_opcao

        botao_iniciar = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_iniciar, 2)
        texto_iniciar = fonte_opcoes.render('Iniciar', True, branco)
        texto_iniciar_rect = texto_iniciar.get_rect(center=botao_iniciar.center)
        tela.blit(texto_iniciar, texto_iniciar_rect)

        x += largura_opcao + espacamento
        botao_configuracoes = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_configuracoes, 2)
        texto_configuracoes = fonte_opcoes.render('Configurações', True, branco)
        texto_configuracoes_rect = texto_configuracoes.get_rect(center=botao_configuracoes.center)
        tela.blit(texto_configuracoes, texto_configuracoes_rect)

        x += largura_opcao + espacamento
        botao_sair = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_sair, 2)
        texto_sair = fonte_opcoes.render('Sair', True, branco)
        texto_sair_rect = texto_sair.get_rect(center=botao_sair.center)
        tela.blit(texto_sair, texto_sair_rect)

        pygame.display.update()

def configuracoes():
    pass

menu_inicial()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da Estrela:")
            print(item)
            if item == None:
                item = "Desconhecido" + str(pos)
            estrelas[item] = pos
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            with open('pontosSalvos.txt','w') as arquivo:
                for estrela, posicao in estrelas.items():
                    arquivo.write(f'{estrela}: {posicao}\n')
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
            estrelas.clear()
            with open('pontosSalvos.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    estrela, posicao = linha.strip().split(':')
                    estrelas[estrela] = eval(posicao)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F12:
            estrelas.clear()

    tela.blit(fundo,(0,0))

    texto = fonte.render('Pressione F10 para salvar os pontos',True,branco)
    tela.blit(texto,(10,10))
    texto2 = fonte.render('Pressione F11 para carregar os pontos',True,branco)
    tela.blit(texto2,(10,30))
    texto2 = fonte.render('Pressione F12 para deletar os pontos',True,branco)
    tela.blit(texto2,(10,50))

    for estrela, posicao in estrelas.items():
        pygame.draw.circle(tela, branco, posicao, 10, 1)  
        texto = fonte.render(estrela, True, branco)
        tela.blit(texto, (posicao[0] + 15, posicao[1]))   

    pygame.display.update()
    relogio.tick(60)
    