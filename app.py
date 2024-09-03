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
G.add_edge("C24", "Elevador", weight=2)
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

#Primeiro Andar
G.add_edge("C26", "Escada A", weight=1)
G.add_edge("C26", "Sala Infra", weight=1)
G.add_edge("C26", "Salão do Juri", weight=7)

G.add_edge("Salão do Juri", "C26",  weight=7)
G.add_edge("Salão do Juri", "C27",  weight=23)
G.add_edge("Salão do Juri", "C53",  weight=4)

G.add_edge("C27", "Salão do Juri",  weight=23)
G.add_edge("C27", "Sala C2",  weight=1)
G.add_edge("C27", "C28",  weight=20)

G.add_edge("C28", "C27",  weight=20)
G.add_edge("C28", "Sala C3",  weight=1)
G.add_edge("C28", "C29",  weight=12)

G.add_edge("C29", "C28",  weight=12)
G.add_edge("C29", "Sala C4",  weight=1)
G.add_edge("C29", "C30",  weight=15)

G.add_edge("C30", "C29",  weight=15)
G.add_edge("C30", "DD102",  weight=1)
G.add_edge("C30", "C31",  weight=15)

G.add_edge("C31", "C30",  weight=15)
G.add_edge("C31", "Auditorio",  weight=1)
G.add_edge("C31", "C33",  weight=14)

G.add_edge("C33", "C31",  weight=14)
G.add_edge("C33", "DD101",  weight=1)
G.add_edge("C33", "DD103",  weight=1)
G.add_edge("C33", "C34",  weight=9)

G.add_edge("C34", "C33",  weight=9)
G.add_edge("C34", "Escada F",  weight=1)
G.add_edge("C34", "C32",  weight=1)

G.add_edge("C32", "C34",  weight=1)
G.add_edge("C32", "Elevador",  weight=1)
G.add_edge("C32", "C35",  weight=2)

G.add_edge("C35", "C32",  weight=2)
G.add_edge("C35", "DD104",  weight=1)
G.add_edge("C35", "C36",  weight=3)

G.add_edge("C36", "C35",  weight=3)
G.add_edge("C36", "DD110",  weight=3)
G.add_edge("C36", "C37",  weight=9)

G.add_edge("C37", "C36",  weight=9)
G.add_edge("C37", "DD109",  weight=1)
G.add_edge("C37", "C38",  weight=7)

G.add_edge("C38", "C37",  weight=7)
G.add_edge("C38", "C38.1",  weight=1)
G.add_edge("C38", "C39",  weight=4)

G.add_edge("C38.1", "Banheiro M",  weight=1)
G.add_edge("C38.1", "Banheiro F",  weight=1)

G.add_edge("C39", "C38",  weight=4)
G.add_edge("C39", "DD106",  weight=1)
G.add_edge("C39", "C40",  weight=3)

G.add_edge("C40", "C39",  weight=3)
G.add_edge("C40", "Escada B",  weight=1)
G.add_edge("C40", "C41",  weight=10)

G.add_edge("C41", "C40",  weight=10)
G.add_edge("C41", "DD105",  weight=1)
G.add_edge("C41", "Audio Visual",  weight=1)
G.add_edge("C41", "C42",  weight=3)

G.add_edge("C42", "C41",  weight=3)
G.add_edge("C42", "DD107",  weight=1)
G.add_edge("C42", "C43",  weight=20)

G.add_edge("C43", "C42",  weight=20)
G.add_edge("C43", "Escada C",  weight=1)
G.add_edge("C43", "C44",  weight=12)

G.add_edge("C44", "C43",  weight=12)
G.add_edge("C44", "Sala E5",  weight=1)
G.add_edge("C44", "C45",  weight=12)

G.add_edge("C45", "C44",  weight=12)
G.add_edge("C45", "Sala E4",  weight=1)
G.add_edge("C45", "C46",  weight=12)

G.add_edge("C46", "C46",  weight=12)
G.add_edge("C46", "Sala E3",  weight=1)
G.add_edge("C46", "C47",  weight=12)

G.add_edge("C47", "C46",  weight=12)
G.add_edge("C47", "Sala E2",  weight=1)
G.add_edge("C47", "C48",  weight=12)

G.add_edge("C48", "C47",  weight=12)
G.add_edge("C48", "Obs. V.E.",  weight=1)
G.add_edge("C48", "C49",  weight=7)

G.add_edge("C49", "C48",  weight=7)
G.add_edge("C49", "Escada D",  weight=1)
G.add_edge("C49", "Lab.07",  weight=1)
G.add_edge("C49", "C50",  weight=22)
G.add_edge("C49", "C54",  weight=13)

G.add_edge("C50", "C49",  weight=22)
G.add_edge("C50", "Lab.06",  weight=22)
G.add_edge("C50", "C51",  weight=13)

G.add_edge("C51", "C50",  weight=13)
G.add_edge("C51", "Lab.05",  weight=1)
G.add_edge("C51", "C52",  weight=13)

G.add_edge("C52", "C51",  weight=13)
G.add_edge("C52", "Lab.04",  weight=1)
G.add_edge("C52", "C53",  weight=13)

G.add_edge("C53", "C52",  weight=13)
G.add_edge("C53", "Lab.03",  weight=1)
G.add_edge("C53", "Salão do Juri",  weight=4)

G.add_edge("C54", "C49",  weight=13)
G.add_edge("C54", "Bloco F",  weight=10)
G.add_edge("C54", "C57",  weight=2)
G.add_edge("C54", "C55",  weight=14)

G.add_edge("C55", "C54",  weight=14)
G.add_edge("C55", "Lab.08",  weight=1)
G.add_edge("C55", "C56",  weight=4)

G.add_edge("C56", "C55",  weight=4)
G.add_edge("C56", "Lab.09",  weight=1)

G.add_edge("C57", "C54",  weight=2)
G.add_edge("C57", "C58",  weight=17)

# Segundo Andar
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
    "C26": "1",
    "C27": "1",
    "C28": "1",
    "C29": "1",
    "C30": "1",
    "C31": "1",
    "C32": "1",
    "C33": "1",
    "C34": "1",
    "C35": "1",
    "C36": "1",
    "C37": "1",
    "C38": "1",
    "C39": "1",
    "C40": "1",
    "C41": "1",
    "C42": "1",
    "C43": "1",
    "C44": "1",
    "C45": "1",
    "C46": "1",
    "C47": "1",
    "C48": "1",
    "C49": "1",
    "C50": "1",
    "C51": "1",
    "C52": "1",
    "C53": "1",
    "C54": "1",
    "C55": "1",
    "C56": "1",
    "C57": "1",
    "C58": "1",
    "Sala Infra": "1",
    "Salão do Juri": "1",
    "Sala C2": "1",
    "Sala C3": "1",
    "Sala C4": "1",
    "DD102": "1",
    "DD103": "1",
    "DD104": "1",
    "DD105": "1",
    "DD106": "1",
    "DD107": "1",
    "DD109": "1",
    "DD110": "1",
    "Auditorio": "1",
    "Banheiro M": "1",
    "Banheiro F": "1",
    "Sala E5": "1",
    "Sala E4": "1",
    "Sala E3": "1",
    "Sala E2": "1",
    "Obs. V.E.": "1",
    "Lab.09": "1",
    "Lab.08": "1",
    "Lab.07": "1",
    "Lab.06": "1",
    "Lab.05": "1",
    "Lab.04": "1",
    "Lab.03": "1",
    "Bloco F": "1",
    
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
    isPCD = request.form.get('pcd')
    
    if isPCD:
        for u, v, data in G.edges(data=True):
            if "Escada" in v or "Escada" in u:
                G[u][v]["weight"] = 100000
    else:
        for u, v, data in G.edges(data=True):
            if "Escada" in v or "Escada" in u:
                G[u][v]["weight"] = 1
                

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