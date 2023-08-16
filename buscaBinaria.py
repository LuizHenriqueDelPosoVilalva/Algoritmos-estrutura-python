#busca a posição de um determinado elemento.

def buscaBinaria(valorBuscado, estrutura):
    inicio = 0
    fim = len(estrutura) -1
    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        if estrutura[meio] == valorBuscado: return meio
        if estrutura[meio] < valorBuscado: inicio = meio + 1
        else: fim = meio - 1
    return -1

est = [1,2,3,4,5,7,9,50]
print(est)
valor = 3

encontrado = buscaBinaria(valor, est)

if encontrado == -1:
    print(f"o elemento {valor} não foi encontrado")
else:
    print(f"o valor {valor} foi encontrado na posição {encontrado}")