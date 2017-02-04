from . entity import *
import os
import pygame


class Paddle(Entity):

	def __init__(self):

		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + "../../res/textures/paddle.png")
		self.__x = 0
		self.__y = 0
		self.__rect = self.__texture.get_rect()


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		self.__rect.left = self.__x
		self.__rect.top = self.__y
		screen.getSurface().blit(self.__texture, self.__rect)
