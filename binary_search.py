# Binary search (log2 n)
def pesquisa_binaria(lista: list[int], item: int):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = int((baixo + alto) / 2)  
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

# TODO: Exercício 1.1 do livro
# 7 etapas (128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1)

# TODO: Exercício 1.2 do livro
# 8 etapas, visto que ao dobrar o tamanho da lista apenas um passo será incrementado.

# Pesquisa Simples = A quantidade de palpites é equivalente a quantidade de itens na lista. (100 Items == 100 palpites)
# Pesquisa Binária = A quantidade de palpites dependerá da quantidade de itens, porém pode ser extremamente minimizado em comparação a pesquisa simples. (100 itens == 7 palpites)
# A pesquisa binária consiste em cortar pela metade a quantidade de possibilidades a cada etapa.
# 4 Bilhões de itens precisariam de no máximo 32 tentativas com a pesquisa binária.
