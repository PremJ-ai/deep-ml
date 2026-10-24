def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	
	#Check matrix dimentions
	for k in range(len(a)):
		if len(a[k]) != len(b):
			return -1  
	
	#Dot product of matrix and vector 
	return [sum(x * w for x, w in zip(row, b)) for row in a]	