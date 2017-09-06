import pygame
from pygame.locals import *
import sys

import globals
import tile

# constants
BLACK = (0, 0, 0)
WINDOW_SIZE = (2400, 1350)

def main():
	# initialize
	pygame.init()
	display = pygame.display
	globals.screen = display.set_mode(( \
			display.Info().current_w / 2, \
			display.Info().current_h / 2))
	display.set_caption("Prototype 2")
	clock = pygame.time.Clock()
	tile.load_map()
	gameover = False

	# game loop
	while not gameover:
		globals.frame += 1

		# cap FPS
		clock.tick(30)

		# handle events
		for event in pygame.event.get():
			if not hasattr(event, 'key'):
				continue
			if event.key == K_ESCAPE:
				gameover = True

		# TODO update

		# render
		globals.screen.fill(BLACK)
		for x in xrange(0x10):
			for y in xrange(0x10):
				tile.map[(x << 4) + y].render(x, y);

		display.flip()

	# cleanup
	sys.exit(0)

if __name__ == "__main__":
	main()
