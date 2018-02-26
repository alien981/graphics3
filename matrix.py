import math


def print_matrix( matrix ):
	s = ""
	q = 0
	while q<len(matrix):
		i = 0
		while i < len(matrix[q]):
			s += str(matrix[q][i]) + " "
			i+=1
		s += "\n"
		q += 1
	print s

def ident( matrix ):
	m = new_matrix(matrix, matrix)
	q = 0
	while q < matrix:
		m[q][q] = 1
		q+=1
	return m



#m1 * m2 -> m2
def matrix_mult( m1, m2 ): # assumes no size issues, error if there are
	m = new_matrix(len(m2[0]), len(m1))
	row = 0
	while (row < len(m1)):
		col = 0
		while (col < len(m2[0])):
			k = 0
			sum = 0
			while (k < len(m2)):
				sum += (m1[row][k]) * (m2[k][col])
				k += 1
			m[row][col] = sum
			col += 1
		row += 1
	return m



def new_matrix(rows, cols ): # 4 and 4 for pt
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''tests
q = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(q)

w = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
e = matrix_mult(q, w)
print_matrix(e)


m = ident(1)
q = ident(7)
print_matrix(m)
print_matrix(q)

m = new_matrix(4, 4)
print_matrix(m)

m[0][0] = 1
m[1][0] = 5
m[2][3] = 6
print_matrix(m)'''
