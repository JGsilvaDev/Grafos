// Informações como prédios, andares e salas
const DATA =
    [
        {
            name: "Prédio Principal",
            andares:
                [
                    {
                        name: "Terreo",
                        salas:
                            [
                                { name: "Xerox", label: "XEROX" },
                                { name: "Capela", label: "CAPELA" },
                                { name: "Pastoral", label: "PASTORAL" },
                                { name: "Diretoria", label: "DIRETORIA" },
                                { name: "Lab. AutoCad", label: "LAB. AUTOCAD" },
                                { name: "Sala Prof. 1", label: "SALA PROF. 1" },
                                { name: "Sala Prof. 2", label: "SALA PROF. 2" },
                                { name: "WC/Vest. M", label: "WC.VEST. M" },
                                { name: "WC/Vest. F", label: "WC.VEST. F" },
                                { name: "Ref./Cantina", label: "CANTINA" },
                                { name: "WC Familia", label: "WC FAMILIA" },
                                { name: "Sala Prof.", label: "SALA PROF." },
                                { name: "Biblioteca", label: "BIBLIOTECA" },
                                { name: "Cant. Leitura", label: "CANT. LEITURA" },
                                { name: "Coordenação", label: "COORDENAÇÃO" },
                                { name: "Secretaria", label: "SECRETARIA" },
                                { name: "Social", label: "SOCIAL" },
                                { name: "Sala Estágio", label: "SALA ESTÁGIO" },
                                { name: "WC Cantina", label: "WC CANTINA" },
                                { name: "Sala Arquivo", label: "SALA ARQUIVO" },
                                { name: "Entrada Prédio M.B.", label: "PRÉDIO M.B." },
                                { name: "Estacionamento", label: "ESTACIONAMENTO" },
                            ]
                    },
                    {
                        name: "Primeiro andar",
                        salas:
                            [
                                { name: "Sala Infra", label: "SALA INFRA" },
                                { name: "Salão do Juri", label: "SALÃO DO JURI" },
                                { name: "Lab.03", label: "LAB.03" },
                                { name: "Lab.04", label: "LAB.04" },
                                { name: "Lab.05", label: "LAB.05" },
                                { name: "Lab.06", label: "LAB.06" },
                                { name: "Sala C2", label: "SALA C2" },
                                { name: "Sala C3", label: "SALA C3" },
                                { name: "Sala C4", label: "SALA C4" },
                                { name: "Obs. V.E.", label: "OBS. V.E." },
                                { name: "Sala E2", label: "SALA E2" },
                                { name: "Sala E3", label: "SALA E3" },
                                { name: "Sala E4", label: "SALA E4" },
                                { name: "Sala E5", label: "SALA E5" },
                                { name: "DD102", label: "DD102" },
                                { name: "DD103", label: "DD103" },
                                { name: "DD104", label: "DD104" },
                                { name: "DD105", label: "DD105" },
                                { name: "DD106", label: "DD106" },
                                { name: "DD107", label: "DD107" },
                                { name: "DD109", label: "DD109" },
                                { name: "Audio Visual", label: "AUDIO VISUAL" },
                                { name: "Banheiro F", label: "BANHEIRO F" },
                                { name: "Banheiro M", label: "BANHEIRO M" },
                                { name: "Auditoria", label: "AUDITORIA" },
                            ]
                    },
                    {
                        name: "Segundo andar",
                        salas:
                        [
                            { name: "Mestrado", label: "Mestrado" },
                            { name: "DD200", label: "sala DD200" },
                            { name: "DD201", label: "sala DD201" },
                            { name: "DD202", label: "sala DD202" },
                            { name: "DD203", label: "sala DD203" },
                            { name: "DD204", label: "sala DD204" },
                            { name: "DD205", label: "sala DD205" },
                            { name: "DD206", label: "sala DD206" },
                            { name: "DD207", label: "sala DD207" },
                            { name: "DD208", label: "sala DD208" },
                            { name: "DD209", label: "sala DD209" },
                            { name: "DD210", label: "sala DD210" },
                            { name: "Banheiros 3", label: "Banheiros 3" },
                            { name: "Coordenação 2", label: "Coordenação 2" }
                        ]
                    }
                ]
        },
        {
            name: "Prédio Mario Bonatti",
            andares:
                [
                    {
                        name: "Térreo",
                        salas:
                            [
                                { name: "Oficina/Aero Unisal", label: "AEROUNISAL" },
                                { name: "Lab. Mec./Projeto", label: "PROJETO" },
                                { name: "Lab. Mecanica", label: "LAB. MECANICA" },
                                { name: "Lab. Civil", label: "LAB. CIVIL" },
                                { name: "Banheiros", label: "BANHEIROS" },
                            ]
                    },
                    {
                        name: "Primeiro Andar",
                        salas:
                            [
                                { name: "LMI", label: "LMI" },
                                { name: "MB07", label: "MB07" },
                                { name: "MB08", label: "MB08" },
                                { name: "MB09", label: "MB09" },
                                { name: "Banheiros 1", label: "BANHEIROS 1" },
                            ]
                    },
                    {
                        name: "Segundo Andar",
                        salas:
                            [
                                { name: "MB01", label: "MB01" },
                                { name: "MB02", label: "MB02" },
                                { name: "MB03", label: "MB03" },
                                { name: "MB04", label: "MB04" },
                                { name: "MB05/MB06", label: "MB05/MB06" },
                                { name: "Banheiros 2", label: "BANHEIROS 2" },
                            ]
                    },
                ]
        },
    ]

const container = document.getElementById("container_predios")

function search(data, filter) {
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
    return salasFiltradas;
}

function loadSearch(data) {
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

document.getElementById('searchInput').addEventListener('input', function () {
    const searchValue = this.value.toUpperCase();
    let salasFiltradas = search(DATA, searchValue)

    loadSearch(salasFiltradas)
});