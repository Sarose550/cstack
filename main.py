from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
first = new_matrix()
ident(first)
csystems = [ first ]
transform = new_matrix()

parse_file( 'script', edges, polygons, transform, csystems, screen, color )