from flask import Flask, render_template, request, jsonify 
import networkx as nx

app = Flask(__name__)

# Criação do grafo
G = nx.Graph()

# Definição das conexões
#Predio Principal
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
G.add_edge("C25", "Entrada Prédio M.B.", weight=1)

G.add_edge("Estacionamento", "Lab. Civil", weight=10)
G.add_edge("Estacionamento", "C105", weight=10)
G.add_edge("Estacionamento", "C25", weight=10)

G.add_edge("Centro", "C0", weight=32)
G.add_edge("Centro", "C1", weight=44)
G.add_edge("Centro", "Corredor S.J.", weight=25)
G.add_edge("Centro", "Ref./Cantina", weight=44)
G.add_edge("Centro", "Sala Prof.", weight=32)
G.add_edge("Centro", "Biblioteca", weight=44)
G.add_edge("Centro", "Coordenação", weight=25)
G.add_edge("Centro", "C19", weight=44)

G.add_edge("Escada A", "C26", weight=1)

G.add_edge("C26", "Sala 201", weight=1)
G.add_edge("C26", "Escada A", weight=1)

G.add_edge("Escada F", "C28", weight=1)
G.add_edge("C28", "Sala 301", weight=1)

# Predio M.B.
G.add_edge("Entrada Prédio M.B.", "C101", weight=13)

G.add_edge("C101", "Entrada Prédio M.B.", weight=13)
G.add_edge("C101", "Lab. Mec./Projeto", weight=5)
G.add_edge("C101", "Saida Prédio M.B.", weight=10)
G.add_edge("C101", "C102", weight=8)

G.add_edge("Lab. Mec./Projeto", "C101", weight=5)

G.add_edge("Saida Prédio M.B.", "C101", weight=10)

G.add_edge("C102", "C101", weight=8)
G.add_edge("C102", "Escada M.B.", weight=5)
G.add_edge("C102", "C103", weight=4)

G.add_edge("Escada M.B.", "C102", weight=5)
G.add_edge("Escada M.B.", "C107", weight=1)

G.add_edge("C103", "C102", weight=4)
G.add_edge("C103", "Elevador M.B.", weight=5)
G.add_edge("C103", "Lab. Mecanica", weight=5)
G.add_edge("C103", "C104", weight=13)

G.add_edge("Elevador M.B.", "C103", weight=5)

G.add_edge("C104", "C103", weight=13)
G.add_edge("C104", "Banheiros", weight=5)
G.add_edge("C104", "Oficina/Aero Unisal", weight=8)

G.add_edge("Oficina/Aero Unisal", "C104", weight=8)

G.add_edge("Banheiros", "C104", weight=5)

G.add_edge("Saida Prédio M.B.", "C105", weight=5)
G.add_edge("C105", "Lab. Civil", weight=49)
G.add_edge("C105", "Estacionamento", weight=10)

G.add_edge("Lab. Civil", "C106", weight=12)
G.add_edge("Lab. Civil", "Estacionamento", weight=10)
G.add_edge("C106", "Lab. Mecanica", weight=40)

G.add_edge("Lab. Mecanica", "103", weight=5)

G.add_edge("C107", "Escada M.B", weight=5)
G.add_edge("C107", "MB09", weight=10)
G.add_edge("C107", "C108", weight=8)

G.add_edge("C108", "C107", weight=8)
G.add_edge("C108", "Elevador M.B.", weight=5)
G.add_edge("C108", "MB08", weight=5)
G.add_edge("C108", "C109", weight=8)

G.add_edge("C109", "C108", weight=8)
G.add_edge("C109", "LMI", weight=5)
G.add_edge("C109", "C110", weight=8)

G.add_edge("C110", "C109", weight=8)
G.add_edge("C110", "MB07", weight=10)
G.add_edge("C110", "Banheiros 1", weight=5)

G.add_edge("C111", "Escada M.B.", weight=5)
G.add_edge("C111", "MB01", weight=6)
G.add_edge("C111", "C112", weight=5)

G.add_edge("MB01", "MB02", weight=6)
G.add_edge("MB01", "C111", weight=6)

G.add_edge("C112", "C111", weight=6)
G.add_edge("C112", "Elevador M.B.", weight=5)
G.add_edge("C112", "MB03", weight=5)
G.add_edge("C112", "C113", weight=3)

G.add_edge("C113", "MB04", weight=5)
G.add_edge("C113", "C112", weight=3)
G.add_edge("C113", "C114", weight=8)

G.add_edge("C114", "C113", weight=8)
G.add_edge("C114", "Banheiros 2", weight=5)
G.add_edge("C114", "MB05/MB06", weight=8)

G.add_edge("Elevador M.B.", "C112", weight=5)

andar_info = {
    # Terreo
    "Portaria": "0",
    "C0": "0",
    "TI": "0",
    "Centro": "0",
    "C20": "0",
    "Xerox": "0",
    "C1": "0",
    "Lab. Info. Geral": "0",
    "Escada A": "0",  
    "Capela": "0",
    "C2": "0",
    "Pastoral": "0",
    "C3": "0",
    "Diretoria": "0",
    "C4": "0",
    "Lab. AutoCad": "0",
    "C5": "0",
    "Corredor S.J.": "0",
    "C6": "0",
    "Sala Prof. 1": "0",
    "C7": "0",
    "Sala Prof. 2": "0",
    "C8": "0",
    "WC/Vest. M": "0",
    "C9": "0",
    "WC/Vest. F": "0",
    "Ref./Cantina": "0",
    "C10": "0",
    "C11": "0",
    "WC Familia": "0",
    "C12": "0",
    "Sala Prof.": "0",
    "C13": "0",
    "Escada B": "0",  
    "Biblioteca": "0",
    "C14": "0",
    "Cant. Leitura": "0",
    "C15": "0",
    "Escada C": "0",  
    "C16": "0",
    "Coordenação": "0",
    "C17": "0",
    "Secretaria": "0",
    "C18": "0",
    "Social": "0",
    "C19": "0",
    "Sala Estágio": "0",
    "C21": "0",
    "C22": "0",
    "C23": "0",
    "C24": "0",
    "Elevador": "0",
    "C25": "0",
    "Estacionamento": "0",
    "Escada F": "0",
    
    # Primeiro andar
    "Sala 201": "1",
    "C26": "1",
    
    # Segundo andar 
    "Sala 301": "2",
    "C28": "2",
    
    # Prédio M.B.
    "Entrada Prédio M.B.": "0",
    "C101": "MB",
    "C102": "MB",
    "C103": "MB",
    "C104": "MB",
    "C105": "MB",
    "C106": "MB",
    "Saida Prédio M.B.": "MB",
    "Lab. Mec./Projeto": "MB",
    "Oficina/Aero Unisal": "MB",
    "Banheiros": "MB",
    "Lab. Mecanica": "MB",
    "Lab. Civil": "MB",
    "Escada M.B.": "MB",
    "Elevador M.B.": "MB",
    
    # Primeiro andar M.B.
    "C107": "MB1",
    "C108": "MB1",
    "C109": "MB1",
    "C110": "MB1",
    "MB07": 'MB1',
    "MB08": 'MB1',
    "MB09": "MB1",
    "Banheiros 1": "MB1",
    "LMI": "MB1",
    
    # Segundo andar M.B.
    "C111": "MB2",
    "C112": "MB2",
    "C113": "MB2",
    "C114": "MB2",
    "MB01": "MB2",
    "MB02": "MB2",
    "MB03": "MB2",
    "MB04": "MB2",
    "Banheiros 2": "MB2",
    
}

# Associar a informação dos andares aos nós
for node, andar in andar_info.items():
    G.nodes[node]['andar'] = andar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salas')
def salas():
    return render_template('salas.html')

@app.route('/mapa', methods=['POST'])
def mapa():
    try:
        # Obtendo as arestas para desenhar no canvas
        arestas = [(u, v, data['weight']) for u, v, data in G.edges(data=True)]
        return jsonify({'arestas': arestas})
    except nx.NetworkXNoPath:
        return jsonify({'arestas': []})
    
@app.route('/mapa')
def mapa_page():
    return render_template('mapa.html')


@app.route('/rota', methods=['POST'])
def rota():
    destino = request.form.get('destino')
    try:
        # Calculando o caminho mais curto a partir da entrada
        caminho = nx.dijkstra_path(G, source='Portaria', target=destino, weight='weight')
        
        # Obter as informações de andar para cada nó no caminho
        andares = [G.nodes[n].get('andar', 'andar padrão') for n in caminho]
        
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