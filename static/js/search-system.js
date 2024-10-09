import { DATA } from './search-data.js'

const container = document.getElementById("container_predios")

export function search(data, filter) {
    console.log("Filtro:", filter);

    const salasFiltradas = data.map(predio => {
        return {
            name: predio.name,
            andares: predio.andares.map(andar => {
                // Filtra as salas que têm o nome desejado
                const salasFiltradas = andar.salas.filter(sala => sala.label.includes(filter));
                return {
                    name: andar.name,
                    salas: salasFiltradas // Mantém apenas as salas filtradas
                };
            }).filter(andar => andar.salas.length > 0) // Remove andares sem salas filtradas
        };
    }).filter(predio => predio.andares.length > 0); // Remove prédios sem andares filtrados

    console.log(salasFiltradas)
    return salasFiltradas;
}

export function loadSearch(data) {
    container.innerHTML = ""


    for (let predio of data) {
        if (predio.andares.length == 0) {
            continue
        }
        const predioDiv = document.createElement('h1')
        predioDiv.className = "predio-title"
        predioDiv.innerHTML = predio.name
        container.appendChild(predioDiv)

        for (let andar of predio.andares) {
            if (andar.salas.length == 0) {
                continue
            }
            const andarDiv = document.createElement('h2')
            andarDiv.className = "andar-title"
            andarDiv.innerHTML = andar.name
            container.appendChild(andarDiv)

            const botoesDestino = document.createElement('div')
            botoesDestino.className = "botoesDestino"

            container.appendChild(botoesDestino)

            for (let sala of andar.salas) {
                botoesDestino.innerHTML += `<button onclick="verRota('${sala.name}')" class="botao">${sala.label}<span class="material-symbols-outlined icon">pin_drop</span></button>`
            }
        }
    }
}

loadSearch(DATA)
search(DATA, "xerox")
search(DATA, "x")

document.getElementById('searchInput').addEventListener('input', function () {
    const searchValue = this.value.toUpperCase();
    let salasFiltradas = search(DATA, searchValue)

    loadSearch(salasFiltradas)
});