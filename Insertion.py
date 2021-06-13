def Insertion_Function(listToBeSorted):
	indexingLength = range(1, len(listToBeSorted))
	for i in indexingLength:
		valueToSort = listToBeSorted[i]
		while listToBeSorted[i-1] > valueToSort and i > 0:
			listToBeSorted[i], listToBeSorted[i-1] = listToBeSorted[i-1], listToBeSorted[i]
			i = i-1
	return listToBeSorted
	
print(Insertion_Function([5,1,9,6,7,4,3,4,5,3,2,3,8,9,4,0]))			
