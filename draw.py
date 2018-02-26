from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
	q = 0
	while q < len(matrix) -1:
		draw_line(matrix[q][0], matrix[q][1], matrix[q+1][0], matrix[q+1][1], screen, color)
		q+=1


def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
	matrix.append([x0, y0, z0])
	matrix.append([x1, y1, z1])	

def add_point( matrix, x, y, z=0 ):
	matrix.append([x, y, z])



def draw_line( x0, y0, x1, y1, screen, color ):
	if x0 == x1 :
		y = y0
		if y < y1:
			while y<y1:
					plot(screen, color, x0, y)
					y +=1
		else:
			while y > y1:
					plot(screen, color, x0, y)
					y -=1			
	elif y0==y1:
		x=x0
		if x < x1:
			while x<x1:
				plot(screen, color, x,y0)
				x+=1
		else:
			while x>x1:
				plot(screen, color, x,y0)
				x-=1


	else:
		if (y0<y1 and x0<x1 and abs(x1-x0) >= abs(y1 - y0) ):
			drawOct1(x0, y0, x1, y1, screen, color)
		elif (y0<y1 and x0<x1 and abs(x1-x0) < abs(y1 - y0) ):
			drawOct2(x0, y0, x1, y1, screen, color)
		elif (y0>y1 and x0<x1 and abs(x1-x0) >= abs(y1 - y0) ):
			drawOct8(x0, y0, x1, y1, screen, color)
		elif (y0>y1 and x0<x1 and abs(x1-x0) < abs(y1 - y0) ):
			drawOct7(x0, y0, x1, y1, screen, color)
		elif (y0>y1 and x0>x1 and abs(x1-x0) < abs(y1 - y0) ): #
			drawOct2(x1, y1, x0, y0, screen, color)
		elif (y0>y1 and x0>x1 and abs(x1-x0) >= abs(y1 - y0) ): #
			drawOct1(x1, y1, x0, y0, screen, color)
		elif (y0<y1 and x0>x1 and abs(x1-x0) >= abs(y1 - y0) ): #
			drawOct8(x1, y1, x0, y0, screen, color)
		else:	#	
			drawOct7(x1, y1, x0, y0, screen, color)
def drawOct1(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = 2 * (y1 - y0)
	B = -2 * (x1 - x0)
	d = 2*A + B
	while x<x1:
		plot(screen, color, x, y)
		if d>0:
			y+=1
			d += 2 * B
		x +=1
		d += 2 * A

	
	
def drawOct2(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = 2 * (y1 - y0)
	B = -2 * (x1 - x0)
	d = A + 2*B
	
	while y<y1:
		plot(screen, color, x,y)
		if d<0:
			x+=1
			d += 2*A
		y+=1
		d += 2*B


def drawOct7(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = 2 * (y1 - y0)
	B = -2 * (x1 - x0)
	d = A-2*B
	while y>=y1:
		plot(screen, color, x, y)
		if d>0:
			x +=1
			d += 2*A
		y -=1
		d -= 2*B

def drawOct8(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = 2 * (y1 - y0)
	B = -2 * (x1 - x0)
	d = 2*A-B
	while y>=y1:
		plot(screen, color, x, y)
		if d<0:
			y -=1
			d -= 2*B
		x +=1
		d += 2*A


