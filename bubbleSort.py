def bubbleSort(estrutura):
    for i in range(0, len(estrutura)):
        for j in range (0, i):
            if estrutura[i] < estrutura[j]:
                temp = estrutura[i]
                estrutura[i] = estrutura[j]
                estrutura[j] = temp
    return estrutura

est = [1,2,6,1,0,10,100,1200]
print(est)
bubbleSort(est)
print(est)