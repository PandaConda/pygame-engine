from pygame import *
from os import *

import globals

set = 0
map = 0
width = 0
height = 0

class Tile:
	image = 0
	solid = 0

	def __init__(self, filepath, solid):
		self.image = image.load(filepath)
		self.solid = solid

	def render(self, x, y):
		global width, height
		globals.screen.blit(self.image, [x * width, y * height])

def resize_set():
	global set, width, height
	width, height = display.get_surface().get_size()
	width /= 16
	height /= 16
	for id in set:
		set[id].image = transform.scale(set[id].image, \
				(width, height))

def load_map():
	global set
	set = {}

	for filename in listdir('res/tile'):
		set[filename.split('.')[0]] \
			= Tile('res/tile/' + filename, True)

	resize_set()

	def tile_border_id(i, a, b, c, d, e):
		if i & c:
			return '4'
		if ((i & a) or (i & b)) and ((i & d) or (i & e)):
			return '3'
		if (i & d) or (i & e):
			return '2'
		if (i & a) or (i & b):
			return '1'
		return '0'

	global map
	map = []

	for i in xrange(0x100):
		id = ''
		id += tile_border_id(i, 0x01, 0x80, 0x40, 0x20, 0x10) # up
		id += tile_border_id(i, 0x40, 0x20, 0x10, 0x08, 0x04) # right
		id += tile_border_id(i, 0x10, 0x08, 0x04, 0x02, 0x01) # down
		id += tile_border_id(i, 0x04, 0x02, 0x01, 0x80, 0x40) # left
		map.append(set[id])
