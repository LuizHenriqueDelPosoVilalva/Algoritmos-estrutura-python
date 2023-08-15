#Busca e ordenação de dados:

def buscarUmValorInteino (valorBuscado, estrutura):
    for i in range(0, len(estrutura)):
        if valorBuscado == estrutura[i]:
            return i
    return -1
        
est = [1,2,5,6,10,11,12]
print(est)
valor = 12
encontrado = buscarUmValorInteino(valor, est)

if encontrado == -1:
    print(f"o elemento {valor} não foi encontrado")
else:
    print(f"o elemento {valor} foi encontrado na posição {encontrado}")

    