def busca_linear(lista, item):
    for i in range(len(minha_lista)):
        if minha_lista[i] == item:
            return i
    return None

minha_lista = [1,3,5,7,9,11]
print(busca_linear(minha_lista, 11))
