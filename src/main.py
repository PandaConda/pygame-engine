from pygame import *
from sys import *

import globals
import tile

# constants
BLACK = (0, 0, 0)
WINDOW_SIZE = (2400, 1350)

def main():
	# initialize
	globals.screen = display.set_mode(WINDOW_SIZE)
	display.set_caption("Prototype 2")
	clock = time.Clock()
	tile.load_map()
	gameover = False

	# game loop
	while not gameover:
		globals.frame += 1

		# cap FPS
		clock.tick(30)

		# handle events
		for e in event.get():
			if not hasattr(e, 'key'):
				continue
			if e.key == K_ESCAPE:
				gameover = True

		# TODO update

		# render
		globals.screen.fill(BLACK)
		for x in xrange(0x10):
			for y in xrange(0x10):
				tile.map[(x << 4) + y].render(x, y);

		display.flip()

	# cleanup
	exit(0)

if __name__ == "__main__":
	main()
