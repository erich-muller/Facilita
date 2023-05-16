function gerarCursoSelecionado(nome) {
    let secao = document.getElementById('cursos-selecionados')
    let div = document.createElement('div')
    div.className = 'botao'
    let curso = document.createElement('p') 
    curso.innerText = nome
    curso.className = 'texto-curso'
    let close_botao = document.createElement('button')
    close_botao.innerText = 'x'
    div.appendChild(close_botao)
    div.appendChild(curso)
    secao.appendChild(div)

    close_botao.addEventListener('click', excluirCurso)
}


// Dados vindos do BD

favoritados = []
lista = document.getElementById('input-array').value.slice(1, -1)
lista = lista.split(', ')
for (li in lista) {
    favoritados.push(lista[li].slice(1,-1))
}


function gerenciador() {   
    let cursos = document.getElementById('input-array')
    let cursos_selecionados = document.getElementById('cursos-selecionados')
    
    // Remover todos os elementos
    while (cursos_selecionados.firstChild) {
        cursos_selecionados.removeChild(cursos_selecionados.lastChild);
    }

    // Recolocar os elementos
    for (i in favoritados) {
        gerarCursoSelecionado(favoritados[i])
    } 

    cursos.value = favoritados
}

gerenciador()


function gerenciarOptions() {
    let inp = document.getElementById('input-field')
    let opt = document.getElementById('options')

    for (o = 0; o < opt.options.length; o++) {
        option = opt.options[o]

        if (inp.value.includes(option.value) && !favoritados.includes(option.value)) {
            favoritados.push(option.value)
            inp.value = ''
        }
    }

    gerenciador()
}

function excluirCurso(event) {
    // Remover da seção
    let opcao = event.target.parentElement
    let section = document.getElementById('cursos-selecionados')
    section.removeChild(opcao)

    // Remover do formulario
    let curso = opcao.getElementsByClassName('texto-curso')[0].innerText
    console.log(curso)
    let index = favoritados.indexOf(curso)
    console.log(index)
    favoritados.splice(index, 1);
    gerenciador()
}