def MeuBubbleSort (estrutura):
    for i in range(len(estrutura)):
        for j in range(0,i):
            if estrutura[i] < estrutura[j]:
                temp = estrutura[i]
                estrutura[i] = estrutura[j]
                estrutura[j] = temp
        return estrutura
    
est = [50,52.2,60,70,30,42,60,90,100,80]
resultado = MeuBubbleSort(est)
print(resultado)