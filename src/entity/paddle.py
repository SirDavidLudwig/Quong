from . entity import *
from core.utils import *
import os
import pygame


class Paddle(Entity):

	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

	def __init__(self, id, direction=LEFT, parent=None):
		super(Paddle, self).__init__(parent)

		self.__id = id

		self.__direction = direction

		self.loadTexture("../../res/textures/paddle.png")
		self.__rect = self.__texture.get_rect()

		self.__width = toPercentWidth(self.getParent(), self.__rect.width)
		self.__height = toPercentHeight(self.getParent(), self.__rect.height)
		self.__minX, self.__maxX = 0, 100
		self.__minY, self.__maxY = 0, 100

		self.initializePosition()


	def initializePosition(self):

		if self.__direction == Paddle.LEFT or self.__direction == Paddle.RIGHT:
			self.setY(50 - self.__height/2)
			self.__minY = self.__width
			self.__maxY = 100 - self.__width - self.__height
		else:
			self.setX(50 - self.__width/2)
			self.__minX = self.__height
			self.__maxX = 100 - self.__width - self.__height

		if self.__direction == Paddle.LEFT:
			self.setX(0)
		elif self.__direction == Paddle.UP:
			self.setY(0)
		elif self.__direction == Paddle.RIGHT:
			self.setX(100-self.__width)
		elif self.__direction == Paddle.DOWN:
			self.setY(100-self.__height)


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		self.__rect.left = toPixelsX(self.getParent(), self.getX())
		self.__rect.top = toPixelsY(self.getParent(), self.getY())
		screen.getSurface().blit(self.__texture, self.__rect)


	def move(self, speed):

		if self.__direction == Paddle.LEFT or self.__direction == Paddle.RIGHT:
			self.setY(self.getY() + speed)
		else:
			self.setX(self.getX() + speed)


	def loadTexture(self, textureFile):
		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + textureFile)

		percentageSize = 15
		scaleFactor = toPixelsHeight(self.getParent(), percentageSize) / self.__texture.get_rect().height
		size = self.__texture.get_rect().size
		self.__texture = pygame.transform.scale(self.__texture, (int(size[0]*scaleFactor), int(size[1]*scaleFactor)))
		self.__texture = pygame.transform.rotate(self.__texture, 90*self.__direction)


	def getId(self):

		return self.__id


	def getPosition(self):

		return (self.getX(), self.getY())


	def getX(self):

		return self.__x


	def getY(self):

		return self.__y


	def setX(self, x):

		if x < self.__minX:
			self.__x = self.__minX
		elif x > self.__maxX:
			self.__x = self.__maxX
		else:
			self.__x = x


	def setY(self, y):

		if y < self.__minY:
			self.__y = self.__minY
		elif y > self.__maxY:
			self.__y = self.__maxY
		else:
			self.__y = y


	def getRect(self):

		return self.__rect
