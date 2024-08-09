import networkx as nx

# Criando o grafo
G = nx.Graph()

# Adicionando nós (salas, elevadores, etc.)
G.add_node("Sala 101", pos=(0, 0, 1))
G.add_node("Corredor 1", pos=(1, 0, 1))
G.add_node("Elevador 1", pos=(2, 0, 1))
G.add_node("Sala 201", pos=(0, 0, 2))
G.add_node("Corredor 2", pos=(1, 0, 2))
G.add_node("Elevador 2", pos=(2, 0, 2))

# Adicionando arestas (conexões entre os nós)
G.add_edge("Sala 101", "Corredor 1", weight=1)
G.add_edge("Corredor 1", "Elevador 1", weight=1)
G.add_edge("Elevador 1", "Elevador 2", weight=1)  # Conecta os andares
G.add_edge("Elevador 2", "Corredor 2", weight=1)
G.add_edge("Corredor 2", "Sala 201", weight=1)

# Função para encontrar a melhor rota usando Dijkstra
def melhor_rota(grafo, origem, destino):
    return nx.dijkstra_path(grafo, origem, destino, weight='weight')

# Exemplo de uso
origem = "Sala 101"
destino = "Elevador 2"
rota = melhor_rota(G, origem, destino)
print(f"Melhor rota de {origem} para {destino}: {rota}")
