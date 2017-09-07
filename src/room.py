import tile

class Room:
	tiles = 0

	def __init__(self, filename):
		file = open('res/room/' + filename + '.room', 'r')

		self.tiles = []

		width = len(file.readline()) + 1
		height = 0

		empty_line = ' ' * width
		tile_data = [empty_line]

		file.seek(0)
		for line in file:
			tile_data.append(' ' + line[:-1] + ' ')
			height += 1

		file.close()

		if height == 0:
			return

		if width == 0:
			self.tiles = [[]] * height
			return

		tile_data.append(empty_line)

		# TODO move to tile.py?
		def get_tile_row(above, row, below):
			def get_tile(tl, t, tr, l, c, r, bl, b, br):
				def empty_tile(type):
					return type in (' ', 'p', 'q')

				if c != '#': return 0
				id = 0x00
				if empty_tile(tl): id |= 0x80
				if empty_tile(t ): id |= 0x40
				if empty_tile(tr): id |= 0x20
				if empty_tile( r): id |= 0x10
				if empty_tile(br): id |= 0x08
				if empty_tile(b ): id |= 0x04
				if empty_tile(bl): id |= 0x02
				if empty_tile( l): id |= 0x01
				return tile.map[id]

			tile_row = []

			for x in xrange(1, width - 1):
				tile_row.append(get_tile(     \
						above[x - 1], \
						above[x],     \
						above[x + 1], \
						  row[x - 1], \
						  row[x],     \
						  row[x + 1], \
						below[x - 1], \
						below[x],     \
						below[x + 1]))

			return tile_row

		for y in xrange(1, height + 1):
			self.tiles.append(get_tile_row(   \
					tile_data[y - 1], \
					tile_data[y],     \
					tile_data[y + 1]))

	def render(self):
		for y in xrange(len(self.tiles)):
			for x in xrange(len(self.tiles[y])):
				if self.tiles[y][x]:
					self.tiles[y][x].render(x, y)
