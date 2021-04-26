from display import *
from draw import *
from parser1 import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = new_matrix()


parse_file( 'script', edges, transform, screen, color )
