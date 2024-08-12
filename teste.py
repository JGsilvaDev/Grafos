import networkx as nx
import pygame

# Criando o grafo
G = nx.Graph()

# Adicionando nós (posições representadas por coordenadas no plano 2D) (x,y)
G.add_node("Port.", pos=(300, 550), tp='S')
G.add_node("Past.", pos=(500, 400), tp='S')      
G.add_node("Secret.", pos=(100, 350), tp='S')    
G.add_node("B1", pos=(500, 300), tp='S') 
G.add_node("B2", pos=(200, 200), tp='S') 
G.add_node("Cant.", pos=(100, 200), tp='S') 
G.add_node("Bibli.", pos=(450, 200), tp='S') 
G.add_node("Mario Bonate", pos=(150, 150), tp='S') 
G.add_node("Quadra", pos=(50, 250), tp='S') 
     
G.add_node("C0", pos=(300, 450), tp='C')
G.add_node("C00", pos=(300, 350), tp='C')        
G.add_node("C4", pos=(300, 250), tp='C')

G.add_node("C1D", pos=(450, 450), tp='C')           
G.add_node("C2D", pos=(450, 400), tp='C')           
G.add_node("C3D", pos=(450, 300), tp='C') 
G.add_node("C4D", pos=(450, 250), tp='C') 

G.add_node("C1E", pos=(150, 450), tp='C')          
G.add_node("C2E", pos=(150, 350), tp='C')           
G.add_node("C3E", pos=(150, 250), tp='C')

G.add_node("C5", pos=(450, 350), tp='C')  
G.add_node("C6", pos=(375, 250), tp='C')   
G.add_node("C7", pos=(150, 200), tp='C')   
          
G.add_node("Escada D", pos=(500, 450), tp='E')      
G.add_node("Escada E", pos=(100, 450), tp='E')   
G.add_node("Escada J", pos=(375, 200), tp='E') 
    
# Adicionando arestas com diferentes pesos (baseados nos tamanhos dos corredores)
G.add_edge("Port.", "C0", weight=1)
 
G.add_edge("C0", "C1D", weight=1)           
G.add_edge("C0", "C1E", weight=1)     
G.add_edge("C0", "C00", weight=1)

G.add_edge("C00", "C0", weight=1)                
G.add_edge("C00", "C5", weight=1)                
G.add_edge("C00", "C2E", weight=1)                
G.add_edge("C00", "C3E", weight=1)                
G.add_edge("C00", "C1D", weight=1)                
G.add_edge("C00", "C4D", weight=1)                
G.add_edge("C00", "C4", weight=1)                
      
G.add_edge("C1D", "Escada D", weight=1)     
G.add_edge("C1D", "C2D", weight=1)
G.add_edge("C1D", "C00", weight=1)

G.add_edge("C1E", "Escada E", weight=1)     
G.add_edge("C1E", "C2E", weight=1)
G.add_edge("C1E", "C00", weight=1)

G.add_edge("C2D", "Past.", weight=1)     
G.add_edge("C2D", "C5", weight=1)  
G.add_edge("C2D", "C1D", weight=1)  
     
G.add_edge("C2E", "Secret.", weight=1)
G.add_edge("C2E", "C3E", weight=1)   
G.add_edge("C2E", "C00", weight=1)   
  
G.add_edge("C3E", "C4", weight=1)
G.add_edge("C3E", "C00", weight=1)
G.add_edge("C3E", "C2E", weight=1)
G.add_edge("C3E", "C7", weight=1)
G.add_edge("C3E", "Quadra", weight=1)

G.add_edge("C3D", "B1", weight=1) 
G.add_edge("C3D", "C4D", weight=1)
G.add_edge("C3D", "C5", weight=1)

G.add_edge("C4D", "C6", weight=1)
G.add_edge("C4D", "C00", weight=1)
G.add_edge("C4D", "C3D", weight=1)
G.add_edge("C4D", "Bibli.", weight=1)

G.add_edge("C4", "C00", weight=1)  
G.add_edge("C4", "C4D", weight=1)  
G.add_edge("C4", "C3E", weight=1)  
 
G.add_edge("C5", "C00", weight=1)
G.add_edge("C5", "C2D", weight=1)
G.add_edge("C5", "C3D", weight=1)

G.add_edge("C6", "C4D", weight=1)
G.add_edge("C6", "C4", weight=1)
G.add_edge("C6", "Escada J", weight=1)

G.add_edge("C7", "C3E", weight=1)
G.add_edge("C7", "B2", weight=1)
G.add_edge("C7", "Cant.", weight=1)
G.add_edge("C7", "Mario Bonate", weight=1)

G.add_edge("Mario Bonate", "C7", weight=1)
G.add_edge("Quadra", "C3E", weight=1)


# Função para encontrar a melhor rota usando Dijkstra
def melhor_rota(grafo, origem, destino):
    return nx.dijkstra_path(grafo, origem, destino, weight='weight')

# Ponto de partida fixo (Portaria)
origem = "Port."

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
destino = "Port."  # Exemplo de destino inicial
rota = atualizar_rota(destino)

# Função para desenhar as conexões (arestas) entre as salas e corredores
def desenhar_conexoes():
    for edge in G.edges:
        inicio = G.nodes[edge[0]]['pos']
        fim = G.nodes[edge[1]]['pos']
        pygame.draw.line(screen, PRETO, inicio, fim, 15)  # Linhas pretas para conectar as salas e corredores

# Função para desenhar a sala como um quadrado
def desenhar_sala(pos, nome, tp):
    x, y = pos
    tipo = tp
    
    fonte = pygame.font.Font(None, 22)
    texto = fonte.render(nome, True, PRETO)
    
    if(tipo == 'C'):
        pygame.draw.rect(screen, PRETO, (x - 15 // 2, y - 15 // 2, 15, 15))
        screen.blit(texto, (x - 20 // 2, y - 20 // 2 - 20))
    elif(tipo == 'E'):
        pygame.draw.rect(screen, VERMELHO, (x - 20 // 2, y - 20 // 2, 20, 20))
        screen.blit(texto, (x - 20 // 2, y - 20 // 2 - 20))
    else:
        pygame.draw.rect(screen, VERDE, (x - 20 // 2, y - 20 // 2, 20, 20))
        screen.blit(texto, (x - 20 // 2, y - 20 // 2 - 20))

# Função para desenhar a rota como uma linha vermelha
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
                destino = "Past."
            elif event.key == pygame.K_2:
                destino = "B1"
            elif event.key == pygame.K_3:
                destino = "Secret."
            elif event.key == pygame.K_6:
                destino = "Port."
            rota = atualizar_rota(destino)
    
    # Desenhar as conexões entre salas e corredores
    desenhar_conexoes()
    
    # Desenhar as salas e corredores
    for node in G.nodes:
        desenhar_sala(G.nodes[node]['pos'], node, G.nodes[node]['tp'])
    
    # Desenhar a rota
    desenhar_rota(rota)
    
    pygame.display.flip()

pygame.quit()
