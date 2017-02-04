from . entity import *
import os
import pygame


class Paddle(Entity):

	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

	def __init__(self, direction=LEFT):
		super(Paddle, self).__init__()

		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + "../../res/textures/paddle.png")
		self.__rect = self.__texture.get_rect()
		self.__direction = direction

		self.__x = 0
		self.__y = 0


	# @param
	# dt: Delta Time
	def draw(self, screen, dt):

		self.__rect.left = self.getX()
		self.__rect.top = self.getY()
		screen.getSurface().blit(self.__texture, self.__rect)


	def move(self, speed):

		print("Moving...")

		if self.__direction == Paddle.RIGHT:
			speed *= -1
		
		if self.__direction == Paddle.UP or self.__direction == Paddle.DOWN:
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
