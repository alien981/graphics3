from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = new_matrix(0, 0)
q = 500
while (q >0):
	add_edge(matrix, q, 0, 0, 0, q, 0)
	q /= 2

draw_lines( matrix, screen, color )

display(screen)
