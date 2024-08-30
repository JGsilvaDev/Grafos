# Projeto de Mapeamento de Rotas Utilizando Grafos

Este projeto é uma aplicação que utiliza grafos para mapear rotas em um edifício com múltiplos andares, permitindo a navegação entre salas através do caminho mais curto calculado pelo algoritmo de Dijkstra.

## Funcionalidades Principais

- **Visualização de Mapa Interativo:** Interface que exibe o layout do edifício, destacando salas, corredores, escadas e elevadores.
- **Cálculo Automático de Rotas:** Utilização do algoritmo de Dijkstra para calcular a rota mais curta entre dois pontos selecionados pelo usuário.
- **Navegação Intuitiva:** Capacidade de selecionar salas de origem e destino para visualizar e seguir a rota calculada.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** NetworkX para representação e manipulação de grafos, Flask para o backend web, HTML/CSS/JavaScript para a interface frontend interativa.

## Como Usar

1. **Instalação:**
   - Clone este repositório: `git clone https://github.com/JGsilvaDev/Grafos.git`
   - Instale as dependências necessárias: `pip install -r requirements.txt`

2. **Execução:**
   - Execute o servidor Flask: `python app.py`
   - Acesse a aplicação através do navegador: `http://localhost:5000`

3. **Interagir com o Mapa:**
   - Clique nas salas para definir pontos de origem e destino.
   - Observe a rota mais curta destacada no mapa.
   - Explore os andares do edifício através de escadas e elevadores.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.
