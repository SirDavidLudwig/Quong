from . entity import *
from core.utils import *
import os
import pygame


class Paddle(Entity):

	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

	def __init__(self, direction=LEFT, parent=None):
		super(Paddle, self).__init__(parent)

		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + "../../res/textures/paddle.png")

		self.__direction = direction
		self.__texture = pygame.transform.rotate(self.__texture, 90*self.__direction)
		self.__rect = self.__texture.get_rect()

		print("Rect width =", self.__rect.width)

		self.__width = toPercentWidth(self.getParent(), self.__rect.width)
		self.__height = toPercentHeight(self.getParent(), self.__rect.height)

		print("% w h =", self.__width, self.__height)

		self.initializePosition()

		print("x y =", self.getX(), self.getY())


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		self.__rect.left = toPixelsX(self.getParent(), self.getX())
		self.__rect.top = toPixelsY(self.getParent(), self.getY())
		screen.getSurface().blit(self.__texture, self.__rect)


	def initializePosition(self):

		if self.__direction == Paddle.LEFT or self.__direction == Paddle.RIGHT:
			self.setY(self.__width)
		else:
			self.setX(self.__height)

		if self.__direction == Paddle.LEFT:
			self.setX(0)
		elif self.__direction == Paddle.UP:
			self.setY(0)
		elif self.__direction == Paddle.RIGHT:
			self.setX(100-self.__width)
		elif self.__direction == Paddle.DOWN:
			self.setY(100-self.__height)

