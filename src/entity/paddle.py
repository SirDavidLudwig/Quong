from . entity import *
import os
import pygame


class Paddle(Entity):

	def __init__(self):
		super(Paddle, self).__init__()

		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + "../../res/textures/paddle.png")
		self.__rect = self.__texture.get_rect()


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		self.__rect.left = self.getX()
		self.__rect.top = self.getY()
		screen.getSurface().blit(self.__texture, self.__rect)
