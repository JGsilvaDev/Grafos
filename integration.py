import networkx as nx
import pygame

# Criando o grafo
G = nx.Graph()

# Adicionando nós (posições representadas por coordenadas no plano 2D)
# CHP - CORREDOR HORIZONTAL PEQUENO
# CVP -    //    VERTICAL     //
# CHM - CORREDOR HORIZONTAL MEDIO
# CVP -    //    VERTICAL    //
# CHG - CORREDOR HORIZONTAL GRANDE
# CVG -    //    VERTICAL    //
# S   - SALA

G.add_node("Portaria", pos=(300, 550), tp='S')      
G.add_node("C0", pos=(300, 450), tp='CVP')            
G.add_node("C1D", pos=(450, 450), tp='CHM')           
G.add_node("C1E", pos=(150, 450), tp='CHM')          
G.add_node("Escada D", pos=(550, 450), tp='E')      
G.add_node("Escada E", pos=(50, 450), tp='E')       
G.add_node("C2D", pos=(450, 300), tp='CVG')           
G.add_node("C2E", pos=(150, 300), tp='CVG')           
G.add_node("C3", pos=(300, 200), tp='CHG')            
G.add_node("Salão", pos=(500, 100), tp='S')         
G.add_node("Lab Info", pos=(50, 100), tp='S')       
G.add_node("Pastoral", pos=(550, 300), tp='S')      
G.add_node("B1", pos=(450, 225), tp='S')            
G.add_node("Secretaria", pos=(50, 300), tp='S')    
G.add_node("C4", pos=(400, 100), tp='CHP')            
G.add_node("C5", pos=(200, 100), tp='CHP')            

# Adicionando arestas com diferentes pesos (baseados nos tamanhos dos corredores)
G.add_edge("Portaria", "C0", weight=1) 
G.add_edge("C0", "C1D", weight=1)           
G.add_edge("C0", "C1E", weight=1)           
G.add_edge("C1D", "Escada D", weight=1)     
G.add_edge("C1E", "Escada E", weight=1)     
G.add_edge("Escada D", "C4", weight=3)     
G.add_edge("Escada E", "C5", weight=3)     
G.add_edge("C1D", "C2D", weight=1)
G.add_edge("C1E", "C2E", weight=1)
G.add_edge("C2D", "Pastoral", weight=1)     
G.add_edge("C2D", "B1", weight=2)           
G.add_edge("C2E", "Secretaria", weight=1)   
G.add_edge("C3", "C4", weight=2)            
G.add_edge("C3", "C5", weight=2)           
G.add_edge("C4", "Salão", weight=1)         
G.add_edge("C5", "Lab Info", weight=1)     

# Função para encontrar a melhor rota usando Dijkstra
def melhor_rota(grafo, origem, destino):
    return nx.dijkstra_path(grafo, origem, destino, weight='weight')

# Ponto de partida fixo (Portaria)
origem = "Portaria"

# Função para atualizar a rota com base em um novo destino
def atualizar_rota(destino):
    try:
        rota = melhor_rota(G, origem, destino)
        print(f"Melhor rota de {origem} para {destino}: {rota}")
        return rota
    except nx.NetworkXNoPath:
        print(f"Não há caminho de {origem} para {destino}.")
        return []

# 2. Renderizar a Maquete em 2D

# Inicializando o PyGame
pygame.init()
display = (620, 600)
screen = pygame.display.set_mode(display)
pygame.display.set_caption("Mapa de Salas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0,0,255)
AMARELO = (255, 255, 0)
MARROM = (139,69,19)
ROXO = (75,0,130)
PRATA = (192,192,192)

# Input para definir o destino
destino = "Portaria"  # Exemplo de destino inicial
rota = atualizar_rota(destino)

# Função para desenhar a sala como um quadrado
def desenhar_sala(pos, nome, tp):
    x, y = pos
    tipo = tp
    
    if(tipo == 'CVP'):
        pygame.draw.rect(screen, MARROM, (x - 40 // 2, y - 40 // 2, 40, 40))
    elif(tipo == 'CHM'):
        pygame.draw.rect(screen, AZUL, (x - 40 // 2, y - 40 // 2, 40, 40))
    elif(tipo == 'CVG'):
        pygame.draw.rect(screen, AMARELO, (x - 40 // 2, y - 40 // 2, 40, 40))
    elif(tipo == 'CHP'):
        pygame.draw.rect(screen, ROXO, (x - 40 // 2, y - 40 // 2, 40, 40))
    elif(tipo == 'CHG'):
        pygame.draw.rect(screen, PRATA, (x - 40 // 2, y - 40 // 2, 40, 40))
    elif(tipo == 'E'):
        pygame.draw.rect(screen, VERMELHO, (x - 40 // 2, y - 40 // 2, 40, 40))
    else:
        pygame.draw.rect(screen, VERDE, (x - 40 // 2, y - 40 // 2, 40, 40))
        
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render(nome, True, PRETO)
    screen.blit(texto, (x - 40 // 2, y - 40 // 2 - 20))

# Função para desenhar a rota como uma linha
def desenhar_rota(rota):
    for i in range(len(rota) - 1):
        inicio = G.nodes[rota[i]]['pos']
        fim = G.nodes[rota[i + 1]]['pos']
        pygame.draw.line(screen, VERMELHO, inicio, fim, 5)

# Loop principal
running = True
while running:
    screen.fill(BRANCO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                destino = "Pastoral"
            elif event.key == pygame.K_2:
                destino = "B1"
            elif event.key == pygame.K_3:
                destino = "Secretaria"
            elif event.key == pygame.K_4:
                destino = "Salão"
            elif event.key == pygame.K_5:
                destino = "Lab Info"
            elif event.key == pygame.K_6:
                destino = "Portaria"
            rota = atualizar_rota(destino)
    
    # Desenhar as salas e corredores
    for node in G.nodes:
        desenhar_sala(G.nodes[node]['pos'], node, G.nodes[node]['tp'])
    
    # Desenhar a rota
    desenhar_rota(rota)
    
    pygame.display.flip()

pygame.quit()
