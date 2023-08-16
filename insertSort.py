def insertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i] #seleção da chave para comparação


		j = i-1 #indice anterior a chave
		#verificação se o elemento anterior é maior que a chave
		while j >= 0 and key < arr[j] :
			#sobrepoe o valor da posição chave
				arr[j + 1] = arr[j]
				#reduz o indice
				j -= 1
		arr[j + 1] = key#guarda o elemento chave


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])