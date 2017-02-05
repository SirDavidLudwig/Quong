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

		self.__width = toPercentWidth(self.getParent(), self.__rect.width)
		self.__height = toPercentHeight(self.getParent(), self.__rect.height)

		self.initializePosition()

		self.__x = 0
		self.__y = 0


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):
		print(self.getX())
		self.__rect.left = toPixelsX(self.getParent(), self.getX())
		self.__rect.top = toPixelsY(self.getParent(), self.getY())
		screen.getSurface().blit(self.__texture, self.__rect)


	def move(self, speed):

		if self.__direction == Paddle.RIGHT:
			speed *= -1
		
		if self.__direction == Paddle.LEFT or self.__direction == Paddle.RIGHT:
			self.setY(self.getY() + speed)
		else:
			self.setX(self.getX() + speed)


	def getX(self):

		return self.__x


	def getY(self):

		return self.__y


	def setX(self, x):

		self.__x = x


	def setY(self, y):
		
		self.__y = y


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