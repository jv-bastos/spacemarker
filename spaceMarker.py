import pygame, math
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
fundo = pygame.image.load('assets/fundo.png')
fundoMenu = pygame.image.load('assets/imagemMenu.jpg')
imagemOficial = pygame.image.load('assets/estrelas.png')
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
botao_mute = None
musica_mutada = False
zoom = 1.0

def menu_inicial():
    global botao_iniciar, botao_configuracoes, botao_sair, estado
    
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

        texto = fonte.render('Alunos: João Vitor Bastos, 1136345', True, branco)
        tela.blit(texto, (10, 10))
        texto = fonte.render('Eduardo Cardoso Debona, 1121865', True, branco)
        tela.blit(texto, (10, 30))
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
        texto_configuracoes = fonte_opcoes.render('Opções', True, branco)
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
    global botao_mute, botao_mostrar_estrelas, musica_mutada, botao_ver_imagem_oficial
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if botao_mute.collidepoint(pos_mouse):
                    musica_mutada = not musica_mutada
                    if musica_mutada:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                elif botao_mostrar_estrelas.collidepoint(pos_mouse):
                    mostrar_estrelas_salvas()
                elif botao_ver_imagem_oficial.collidepoint(pos_mouse):
                    visualizar_imagem_oficial()
                elif botao_voltar.collidepoint(pos_mouse):
                    rodando = False

        tela.blit(fundoMenu, (0, 0))

        texto_titulo = fonte_titulo.render('Opções', True, branco)
        titulo_rect = texto_titulo.get_rect(center=(tela.get_width() // 2, 100))
        tela.blit(texto_titulo, titulo_rect)

        largura_opcao = 250
        altura_opcao = 50
        espacamento = 20
        margem_inferior = 100

        x = (tela.get_width() - largura_opcao) // 2
        y = tela.get_height() - margem_inferior - altura_opcao * 3 - espacamento * 2

        botao_mute = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_mute, 2)
        texto_mute = fonte_opcoes.render('Mutar Música' if not musica_mutada else 'Desmutar Música', True, branco)
        texto_mute_rect = texto_mute.get_rect(center=botao_mute.center)
        tela.blit(texto_mute, texto_mute_rect)

        y += altura_opcao + espacamento
        botao_mostrar_estrelas = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_mostrar_estrelas, 2)
        texto_mostrar_estrelas = fonte_opcoes.render('Estrelas Salvas', True, branco)
        texto_mostrar_estrelas_rect = texto_mostrar_estrelas.get_rect(center=botao_mostrar_estrelas.center)
        tela.blit(texto_mostrar_estrelas, texto_mostrar_estrelas_rect)

        y += altura_opcao + espacamento
        botao_ver_imagem_oficial = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_ver_imagem_oficial, 2)
        texto_ver_imagem_oficial = fonte_opcoes.render('Imagem Oficial', True, branco)
        texto_ver_imagem_oficial_rect = texto_ver_imagem_oficial.get_rect(center=botao_ver_imagem_oficial.center)
        tela.blit(texto_ver_imagem_oficial, texto_ver_imagem_oficial_rect)

        y += altura_opcao + espacamento
        botao_voltar = pygame.Rect(x, y, largura_opcao, altura_opcao)
        pygame.draw.rect(tela, branco, botao_voltar, 2)
        texto_voltar = fonte_opcoes.render('Voltar', True, branco)
        texto_voltar_rect = texto_voltar.get_rect(center=botao_voltar.center)
        tela.blit(texto_voltar, texto_voltar_rect)

        pygame.display.update()

def visualizar_imagem_oficial():
    global zoom
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 4:
                    zoom += 0.1
                elif evento.button == 5:
                    zoom = max(0.1, zoom - 0.1)
        
        tela.fill(preto)
        
        largura_original = int(imagemOficial.get_width() * zoom)
        altura_original = int(imagemOficial.get_height() * zoom)
        imagem_redimensionada = pygame.transform.scale(imagemOficial, (largura_original, altura_original))
        
        pos_x = (tela.get_width() - largura_original) // 2
        pos_y = (tela.get_height() - altura_original) // 2
        
        tela.blit(imagem_redimensionada, (pos_x, pos_y))
        
        pygame.display.update()

def mostrar_estrelas_salvas():
    rodando = True
    scroll_y = 0
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 4:
                    scroll_y = min(scroll_y + 20, 0)
                elif evento.button == 5:
                    scroll_y = max(scroll_y - 20, -(len(estrelas) * 30 - tela.get_height() + 100))

        tela.fill(preto)
        
        texto_titulo = fonte_titulo.render('Estrelas Salvas', True, branco)
        titulo_rect = texto_titulo.get_rect(center=(tela.get_width() // 2, 50))
        tela.blit(texto_titulo, titulo_rect)

        y = 100 + scroll_y
        for estrela, posicao in estrelas.items():
            texto_estrela = fonte.render(f'{estrela}: {posicao}', True, branco)
            tela.blit(texto_estrela, (50, y))
            y += 30

        texto_voltar = fonte.render('Pressione ESC para voltar', True, branco)
        tela.blit(texto_voltar, (50, y + 30))
        texto = fonte.render('Obs: Não será possível listar as estrelas caso você tenha usado a função de deletar os pontos.',True,branco)
        tela.blit(texto,(10,610))
        texto2 = fonte.render('Caso tenha feito isso, retorne para a tela das estrelas e carregue os pontos salvos novamente.',True,branco)
        tela.blit(texto2,(10,630))

        pygame.display.update()

def distancia_entre_pontos(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def distancia_ponto_para_linha(px, py, x1, y1, x2, y2):
    num = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1)
    den = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return num / den

menu_inicial()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring("Space", "Nome da Estrela:")
                if item is None:
                    item = "Desconhecido" + str(pos)
                estrelas[item] = pos
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            with open('pontosSalvos.txt', 'w') as arquivo:
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
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            menu_inicial()

    tela.blit(fundo, (0, 0))

    texto = fonte.render('Pressione F10 para salvar os pontos', True, branco)
    tela.blit(texto, (10, 30))
    texto = fonte.render('Pressione F11 para carregar os pontos', True, branco)
    tela.blit(texto, (10, 50))
    texto = fonte.render('Pressione F12 para deletar os pontos', True, branco)
    tela.blit(texto, (10, 70))
    texto = fonte.render('Pressione ESC para voltar ao menu inicial', True, branco)
    tela.blit(texto, (10, 10))

    ultima_posicao = None
    for estrela, posicao in estrelas.items():
        pygame.draw.circle(tela, branco, posicao, 10, 1)
        texto = fonte.render(estrela, True, branco)
        tela.blit(texto, (posicao[0] + 15, posicao[1]))

        if ultima_posicao is not None:
            pygame.draw.line(tela, branco, ultima_posicao, posicao, 1)
        
            mouse_pos = pygame.mouse.get_pos()
            distancia_mouse_linha = distancia_ponto_para_linha(
                mouse_pos[0], mouse_pos[1],
                ultima_posicao[0], ultima_posicao[1],
                posicao[0], posicao[1]
            )
            
            if distancia_mouse_linha < 5:
                distancia = distancia_entre_pontos(ultima_posicao, posicao)
                distancia_texto = fonte.render(f'{distancia:.2f}', True, branco)
                distancia_texto_rect = distancia_texto.get_rect(center=((ultima_posicao[0] + posicao[0]) // 2, (ultima_posicao[1] + posicao[1]) // 2))
                tela.blit(distancia_texto, distancia_texto_rect)

        ultima_posicao = posicao

    pygame.display.update()
    relogio.tick(60)
