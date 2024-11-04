import pygame
import random

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo das Capitais")

paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Japão": "Tóquio",
    "Estados Unidos": "Washington, D.C.",
    "Argentina": "Buenos Aires",
    "Reino Unido": "Londres",
    "Canadá": "Ottawa",
    "Itália": "Roma",
    "Austrália": "Canberra",
    "Índia": "Nova Délhi",
    "Rússia": "Moscou",
    "China": "Pequim",
    "México": "Cidade do México",
}

def exibir_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    superficie = fonte.render(texto, True, cor)
    tela.blit(superficie, (x, y))

def jogar():
    pontos = 0
    paises = list(paises_capitais.keys())

    imagem_brasil = pygame.image.load("brasil.gif")
    imagem_brasil = pygame.transform.scale(imagem_brasil, (150, 150))

    rodando = True
    while rodando:
        tela.fill((255, 255, 255))

        pais_correspondente = random.choice(paises)
        resposta_correta = paises_capitais[pais_correspondente]
        
        opcoes = [resposta_correta]
        while len(opcoes) < 3:
            opcao_errada = random.choice(list(paises_capitais.values()))
            if opcao_errada not in opcoes:
                opcoes.append(opcao_errada)

        random.shuffle(opcoes)

        exibir_texto(f"Qual é a capital do {pais_correspondente}?", 40, (0, 0, 0), 50, 250)

        resposta_usuario = None
        while resposta_usuario is None:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    resposta_usuario = 0

                if evento.type == pygame.KEYDOWN:
                    if evento.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                        resposta_usuario = evento.unicode

            for i, opcao in enumerate(opcoes):
                cor_opcao = (0, 0, 255) if resposta_usuario == str(i + 1) else (0, 0, 0)
                exibir_texto(f"{i + 1}. {opcao}", 30, cor_opcao, 50, 300 + i * 40)

            tela.blit(imagem_brasil, (600, 50))
            pygame.display.flip()

        if opcoes[int(resposta_usuario) - 1] == resposta_correta:
            pontos += 1
            resultado_texto = "Você acertou!"
        else:
            resultado_texto = f"Você errou! A capital do {pais_correspondente} é {resposta_correta}."

        tela.fill((255, 255, 255))
        exibir_texto(resultado_texto, 40, (0, 128, 0) if "acertou" in resultado_texto else (255, 0, 0), 50, 250)
        exibir_texto(f"Pontos: {pontos}", 30, (0, 0, 0), 50, 300)
        pygame.display.flip()
        pygame.time.delay(3000)

    pygame.quit()

if __name__ == "__main__":
    jogar()
