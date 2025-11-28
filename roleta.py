import pygame
import random
import time

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("roleta")


fonte_pais = pygame.font.Font.italic(None, 48) 
fonte_botao = pygame.font.Font(None, 36) 

PAISES = [
    "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola",
    "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia",
    "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados",
    "Barém", "Bélgica", "Belize", "Benin", "Bielorrússia", "Bolívia",
    "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária",
    "Burkina Faso", "Burundi", "Butão", "Cabo Verde", "Camboja", "Camarões",
    "Canadá", "Cazaquistão", "Chade", "Chile", "China", "Chipre", "Colômbia",
    "Comores", "Coreia do Norte", "Coreia do Sul", "Costa do Marfim",
    "Costa Rica", "Croácia", "Cuba", "Dinamarca", "Djibuti", "Dominica",
    "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia",
    "Eslováquia", "Eslovênia", "Espanha", "Estados Unidos", "Estônia",
    "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", "Gâmbia",
    "Geórgia", "Gana", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné",
    "Guiné-Bissau", "Guiné Equatorial", "Haiti", "Honduras", "Hungria",
    "Iêmen", "Ilhas Marshall", "Ilhas Salomão", "Índia", "Indonésia", "Irã",
    "Iraque", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão",
    "Jordânia", "Kuwait", "Laos", "Lesoto", "Letônia", "Líbano", "Libéria",
    "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte",
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos",
    "Maurícia", "Mauritânia", "México", "Micronésia", "Moçambique", "Moldávia",
    "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal",
    "Nicarágua", "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã",
    "Países Baixos", "Palau", "Panamá", "Papua-Nova Guiné", "Paquistão",
    "Paraguai", "Peru", "Polônia", "Portugal", "Catar", "Quênia", "Quirguistão",
    "Quiribati", "Reino Unido", "República Centro-Africana",
    "República Democrática do Congo", "República Dominicana", "República Tcheca",
    "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia",
    "São Cristóvão e Neves", "São Tomé e Príncipe", "São Vicente e Granadinas",
    "Senegal", "Serra Leoa", "Sérvia", "Seicheles", "Singapura", "Síria",
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça",
    "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", "Timor-Leste", "Togo",
    "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia",
    "Tuvalu", "Ucrânia", "Uganda", "Uruguai", "Uzbequistão", "Vanuatu",
    "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]

sorteando = False
pais_atual = "Clique em Sortear!"
pais_final = ""
tempo_inicio_sorteio = 0
DURACAO_SORTEIO = 5 

largura_botao = 150
altura_botao = 50
pos_botao_x = LARGURA // 2 - largura_botao // 2
pos_botao_y = ALTURA - 100
rect_botao = pygame.Rect(pos_botao_x, pos_botao_y, largura_botao, altura_botao)


def desenhar_texto(superficie, texto, fonte, cor, x, y):
    """Função auxiliar para renderizar e desenhar texto."""
    texto_surf = fonte.render(texto, True, cor)
    texto_rect = texto_surf.get_rect(center=(x, y))
    superficie.blit(texto_surf, texto_rect)

def desenhar_roleta(superficie):
    """Desenha o país atual no centro da tela."""
    superficie.fill(PRETO)

    desenhar_texto(superficie, pais_atual, fonte_pais, BRANCO, LARGURA // 2, ALTURA // 2)

    cor_botao = VERMELHO if sorteando else (0, 150, 0)
    pygame.draw.rect(superficie, cor_botao, rect_botao, 0, 10)
    texto_botao = "Sorteando..." if sorteando else "Sortear!"
    desenhar_texto(superficie, texto_botao, fonte_botao, BRANCO, LARGURA // 2, pos_botao_y + altura_botao // 2)

    if not sorteando and pais_final:
        desenhar_texto(superficie, f"Vencedor: {pais_final}", fonte_botao, VERMELHO, LARGURA // 2, ALTURA // 2 + 50)
    
    pygame.display.flip()

rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
       
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            if rect_botao.collidepoint(evento.pos) and not sorteando:
                sorteando = True
                tempo_inicio_sorteio = time.time()
                pais_final = random.choice(PAISES) 

    if sorteando:
        tempo_decorrido = time.time() - tempo_inicio_sorteio
        
        #ritmo
        atraso_minimo = 0.02
        atraso_maximo = 0.2

        fator_desaceleracao = min(tempo_decorrido / DURACAO_SORTEIO, 1.0)
        atraso_atual = atraso_minimo + (atraso_maximo - atraso_minimo) * fator_desaceleracao
        
        if tempo_decorrido < DURACAO_SORTEIO:

            if random.random() < 1.0 - fator_desaceleracao: 
                pais_atual = random.choice(PAISES)
        else:

            sorteando = False
            pais_atual = pais_final 
            
    desenhar_roleta(tela)

    clock.tick(60)

pygame.quit()