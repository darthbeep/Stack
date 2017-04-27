from stack import Stack
from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
poly = []
transform = new_matrix()
stack = Stack()
# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, poly, transform, screen, color, stack )
