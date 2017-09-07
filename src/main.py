import pygame
from pygame.locals import *
import sys

import color
import globals
from room import Room
import tile

def main():
	# initialize
	pygame.init()
	display = pygame.display
	globals.screen = display.set_mode(( \
			display.Info().current_w / 2, \
			display.Info().current_h / 2))
	display.set_caption('Prototype 2')
	clock = pygame.time.Clock()
	tile.load_map()
	tile.resize_set()
	room = Room('test')
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
		globals.screen.fill(color.RED)
		room.render()
		display.flip()

	# cleanup
	sys.exit(0)

if __name__ == "__main__":
	main()
