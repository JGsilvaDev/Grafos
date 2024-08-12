import networkx as nx
import pygame
import math
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

# Dados fictícios para o modelo
# Características dos nós (x1, y1, x2, y2) e rótulos (1 se existe aresta, 0 caso contrário)
features = []
labels = []

for u, v in G.edges():
    x1, y1 = G.nodes[u]['pos']
    x2, y2 = G.nodes[v]['pos']
    features.append([x1, y1, x2, y2])
    labels.append(1)

# Adicionando exemplos negativos (arestas ausentes) com características aleatórias
import random
nodes = list(G.nodes())
for _ in range(100):
    u, v = random.sample(nodes, 2)
    if not G.has_edge(u, v):
        x1, y1 = G.nodes[u]['pos']
        x2, y2 = G.nodes[v]['pos']
        features.append([x1, y1, x2, y2])
        labels.append(0)

features = np.array(features)
labels = np.array(labels)

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Função para prever a presença de uma aresta
def prever_conexao(node1, node2):
    x1, y1 = G.nodes[node1]['pos']
    x2, y2 = G.nodes[node2]['pos']
    features = np.array([[x1, y1, x2, y2]])
    prediction = model.predict(features)
    return prediction[0] == 1

# Testar a previsão de uma nova conexão
novo_destino = "Cant."
if prever_conexao(origem, novo_destino):
    print(f"Previsão: Existe uma conexão entre {origem} e {novo_destino}.")
else:
    print(f"Previsão: Não existe uma conexão entre {origem} e {novo_destino}.")

# Atualizar a rota para o novo destino
rota_atualizada = atualizar_rota(novo_destino)

# Configurações do pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Função para desenhar o grafo
def desenhar_grafo(grafo, screen):
    pos = nx.get_node_attributes(grafo, 'pos')
    
    # Desenhar as arestas
    for edge in grafo.edges():
        inicio = pos[edge[0]]
        fim = pos[edge[1]]
        pygame.draw.line(screen, (0, 0, 0), inicio, fim, 2)  # Desenha a linha entre os nós
    
    # Desenhar os nós
    for node, (x, y) in pos.items():
        pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 10)  # Desenha o nó
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(node, True, (255, 255, 255))
        screen.blit(texto, (x - 10, y - 10))  # Desenha o texto do nó

# Configurações do pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Criando o grafo e adicionando nós e arestas
G = nx.Graph()
# Adicione nós e arestas aqui, como no código fornecido...

# Loop principal do pygame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    desenhar_grafo(G, screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()