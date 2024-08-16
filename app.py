from flask import Flask, render_template, request, jsonify 
import networkx as nx

app = Flask(__name__)

# Criação do grafo
G = nx.Graph()

# Definição das conexões
G.add_edge("Portaria", "C0", weight=6)

G.add_edge("C0", "TI", weight=11)
G.add_edge("C0", "Centro", weight=32)
G.add_edge("C0", "C20", weight=28)

G.add_edge("TI", "C0", weight=11)
G.add_edge("TI", "Xerox", weight=11)

G.add_edge("Xerox", "TI", weight=11)
G.add_edge("Xerox", "C1", weight=6)

G.add_edge("C1", "Xerox", weight=6)
G.add_edge("C1", "Lab. Info. Geral", weight=1)
G.add_edge("C1", "Escada A", weight=1)
G.add_edge("C1", "Capela", weight=1)
G.add_edge("C1", "C2", weight=7)
G.add_edge("C1", "Centro", weight=44)

G.add_edge("C2", "Pastoral", weight=1)
G.add_edge("C2", "C1", weight=7)
G.add_edge("C2", "C3", weight=11)

G.add_edge("C3", "Diretoria", weight=1)
G.add_edge("C3", "C2", weight=11)
G.add_edge("C3", "C4", weight=11)

G.add_edge("C4", "Lab. AutoCad", weight=1)
G.add_edge("C4", "C3", weight=11)
G.add_edge("C4", "C5", weight=6)

G.add_edge("C5", "Corredor S.J.", weight=1)
G.add_edge("C5", "C4", weight=6)
G.add_edge("C5", "C6", weight=6)
G.add_edge("C5", "Centro", weight=25)

G.add_edge("C6", "Sala Prof. 1", weight=1)
G.add_edge("C6", "C5", weight=6)
G.add_edge("C6", "C7", weight=6)

G.add_edge("C7", "Sala Prof. 2", weight=1)
G.add_edge("C7", "C6", weight=6)
G.add_edge("C7", "C8", weight=11)

G.add_edge("C8", "WC/Vest. M", weight=1)
G.add_edge("C8", "C7", weight=11)
G.add_edge("C8", "C9", weight=11)

G.add_edge("C9", "WC/Vest. F", weight=1)
G.add_edge("C9", "C8", weight=11)
G.add_edge("C9", "Ref./Cantina", weight=5)

G.add_edge("Ref./Cantina", "Quadra", weight=18)
G.add_edge("Ref./Cantina", "C10", weight=10)
G.add_edge("Ref./Cantina", "C9", weight=10)
G.add_edge("Ref./Cantina", "Centro", weight=10)

G.add_edge("C10", "Ref./Cantina", weight=10)
G.add_edge("C10", "C21", weight=7)
G.add_edge("C10", "C11", weight=10)

G.add_edge("C11", "WC Familia", weight=1)
G.add_edge("C11", "C10", weight=14)
G.add_edge("C11", "C12", weight=8)

G.add_edge("C12", "Sala Prof.", weight=1)
G.add_edge("C12", "C11", weight=8)
G.add_edge("C12", "C13", weight=22)
G.add_edge("C12", "Centro", weight=32)

G.add_edge("C13", "Escada B", weight=1)
G.add_edge("C13", "C12", weight=22)
G.add_edge("C13", "Biblioteca", weight=5)

G.add_edge("Biblioteca", "C13", weight=5)
G.add_edge("Biblioteca", "C14", weight=6)
G.add_edge("Biblioteca", "Centro", weight=44)

G.add_edge("C14", "Cant. Leitura", weight=1)
G.add_edge("C14", "Biblioteca", weight=6)
G.add_edge("C14", "C15", weight=6)

G.add_edge("C15", "Escada C", weight=1)
G.add_edge("C15", "C14", weight=6)
G.add_edge("C15", "C16", weight=6)

G.add_edge("C16", "Coordenação", weight=1)
G.add_edge("C16", "C17", weight=26)
G.add_edge("C16", "Centro", weight=26)

G.add_edge("C17", "Secretaria", weight=1)
G.add_edge("C17", "C16", weight=26)
G.add_edge("C17", "C18", weight=11)

G.add_edge("C18", "Social", weight=1)
G.add_edge("C18", "C17", weight=11)
G.add_edge("C18", "C19", weight=7)

G.add_edge("C19", "Escada D", weight=1)
G.add_edge("C19", "C18", weight=7)
G.add_edge("C19", "C20", weight=1)
G.add_edge("C19", "Centro", weight=44)

G.add_edge("C20", "Sala Estágio", weight=1)
G.add_edge("C20", "C19", weight=1)
G.add_edge("C20", "C0", weight=28)

G.add_edge("C21", "WC Cantina", weight=1)
G.add_edge("C21", "C10", weight=7)
G.add_edge("C21", "C22", weight=11)

G.add_edge("C22", "C21", weight=11)
G.add_edge("C22", "C23", weight=4)
G.add_edge("C22", "C25", weight=12)

G.add_edge("C23", "Escada F", weight=1)
G.add_edge("C23", "C22", weight=4)
G.add_edge("C23", "C24", weight=5)

G.add_edge("C24", "Sala Arquivo", weight=1)
G.add_edge("C24", "Elevador", weight=1)
G.add_edge("C24", "C23", weight=5)

G.add_edge("C25", "C22", weight=12)
G.add_edge("C25", "Estacionamento", weight=1)
G.add_edge("C25", "Prédio M.B.", weight=1)

G.add_edge("Centro", "C0", weight=32)
G.add_edge("Centro", "C1", weight=44)
G.add_edge("Centro", "Corredor S.J.", weight=25)
G.add_edge("Centro", "Ref./Cantina", weight=44)
G.add_edge("Centro", "Sala Prof.", weight=32)
G.add_edge("Centro", "Biblioteca", weight=44)
G.add_edge("Centro", "Coordenação", weight=25)
G.add_edge("Centro", "C19", weight=44)

G.add_edge("Escada A", "Sala 201", weight=1)

andar_info = {
    "Portaria": "1",
    "C0": "1",
    "TI": "1",
    "Centro": "1",
    "C20": "1",
    "Xerox": "1",
    "C1": "1",
    "Lab. Info. Geral": "1",
    "Escada A": "1",  # Conecta ao segundo andar
    "Capela": "1",
    "C2": "1",
    "Pastoral": "1",
    "C3": "1",
    "Diretoria": "1",
    "C4": "1",
    "Lab. AutoCad": "1",
    "C5": "1",
    "Corredor S.J.": "1",
    "C6": "1",
    "Sala Prof. 1": "1",
    "C7": "1",
    "Sala Prof. 2": "1",
    "C8": "1",
    "WC/Vest. M": "1",
    "C9": "1",
    "WC/Vest. F": "1",
    "Ref./Cantina": "1",
    "C10": "1",
    "C11": "1",
    "WC Familia": "1",
    "C12": "1",
    "Sala Prof.": "1",
    "C13": "1",
    "Escada B": "1",  # Conecta ao segundo andar
    "Biblioteca": "1",
    "C14": "1",
    "Cant. Leitura": "1",
    "C15": "1",
    "Escada C": "1",  # Conecta ao segundo andar
    "C16": "1",
    "Coordenação": "1",
    "C17": "1",
    "Secretaria": "1",
    "C18": "1",
    "Social": "1",
    "C19": "1",
    "Sala Estágio": "1",
    "C21": "1",
    "C22": "1",
    "C23": "1",
    "C24": "1",
    "Elevador": "1",  # Conecta ao segundo andar
    "C25": "1",
    "Estacionamento": "1",
    "Prédio M.B.": "1",

    # Segundo andar (exemplos)
    "Sala 201": "2",
    "Sala 202": "2",
    "Sala 203": "2",
    "C26": "2",
    "C27": "2",
}

# Adicionando essa informação ao grafo
nx.set_node_attributes(G, andar_info, 'andar')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rota', methods=['POST'])
def rota():
    destino = request.form.get('destino')
    try:
        # Calculando o caminho mais curto a partir da entrada
        caminho = nx.dijkstra_path(G, source='Portaria', target=destino, weight='weight')
        
        # Obter as informações de andar para cada nó no caminho
        andares = [G.nodes[n]['andar'] for n in caminho]
        
        # Obtendo as arestas para desenhar no canvas
        arestas = [(u, v, data['weight']) for u, v, data in G.edges(data=True)]
        return jsonify({'rota': caminho, 'andares': andares, 'arestas': arestas})
    except nx.NetworkXNoPath:
        return jsonify({'rota': [], 'andares': [], 'arestas': []})


@app.route('/rota', methods=['GET'])
def rota_page():
    return render_template('rota.html')

if __name__ == '__main__':
    app.run(debug=True)
    # host='192.168.171.194'