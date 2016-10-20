def det(matrix):
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
	else:
		determinant=0
		for i in range(len(matrix)):
			b=[]
			c=range(len(matrix))
			c.remove(i)
			for j in range(1,len(matrix)):
				h=[]
				for k in c:
					h.append(matrix[j][k])
				b.append(h)
			determinant = determinant + det(b)*((-1)**(i))*(matrix[0][i])
		return determinant