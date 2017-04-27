from display import *
from matrix import *
from draw import *
from copy import *

#Base courtesy of http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html

#The point of creating my own stack is that I can do whatever I want with it easily
#Also idk how to use python

class Stack:
	def __init__(self):
	    ma = new_matrix()
	    ident(ma)
	    self.items = [ma]

	def isEmpty(self):
		#self.type = []
		return self.items == []

	def push(self):
		self.items.append(deepcopy(self.peekMatrix()))
		#self.displayStack()

	def pop(self):
		self.items.pop()
		return self

	def peekMatrix(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)-1

	def emptyStack(self):
		while not(isEmpty(self)):
			pop(self)

	def printStack(self, screen, color):
		""
		#while not(self.isEmpty()):
		#	#print self.size()
		#	if self.peekType() == 'p':
		#		draw_polygons(self.peekMatrix(), screen, color)
		#	if self.peekType() == 'e':
		#		draw_lines(self.peekMatrix(), screen, color)
		#	self.pop()
		#	self.pop()

	def displayStack(self):
		print [self.items[self.size()]]

	def matrixify(self, m):
		matrix_mult(self.peekMatrix(), m)
		self.items[self.size()]=m

	def drawPoly(self, m, screen, color):
            matrix_mult(self.peekMatrix(), m)
            draw_polygons(m, screen, color)

	def drawLine(self, m, screen, color):
            matrix_mult(self.peekMatrix(), m)
            draw_lines(m, screen, color)
