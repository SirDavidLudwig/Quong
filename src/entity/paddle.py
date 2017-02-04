from . entity import *
import pygame


class Paddle(Entity):

	def __init__(self):

		pass


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		pygame.draw.rect(screen.getSurface(), (0, 128, 255), pygame.Rect(0, 0, screen.getWidth(), screen.getHeight()))
