#ball.py
from . entity import *
import os
import random
import pygame
import math


class Ball(Entity):

	def __init__(self, parent):

		super(Ball, self).__init__(parent)
		unitVecX = random.uniform(-1.0, 1.0)
		unitVecY = random.choice((-1, 1)) * math.sqrt(1-unitVecX**2)
		self.__unitVec = (unitVecX, unitVecY)
		self.__speed = 20

		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		percentSize = 10
		self.__texture = pygame.image.load(base_path + "../../res/textures/ball.png")
		print(self.__texture)
		size = self.__texture.get_rect().size
		scaleFactor = percentSize/size[0]
		self.__width = percentSize
		pygame.transform.scale(self.__texture, (int(size[0]*scaleFactor), int(size[1]*scaleFactor)))
		self.__rect = self.__texture.get_rect()

		self.setX(50 - self.__width/2)
		self.setY(50 - self.__width/2)


	def draw(self, screen, dt):

		self.setX(self.getX() + self.getVelocity()[0] * dt)
		self.setY(self.getY() + self.getVelocity()[1] * dt)
		self.__rect.left = toPixelsX(self.getParent(), self.getX())
		self.__rect.top = toPixelsY(self.getParent(), self.getY())
		screen.getSurface().blit(self.__texture, self.__rect)


	def getUnitVec(self):

		return self.__unitVec


	def getSpeed(self):

		return self.__speed


	def getVelocity(self):

		return tuple((i*self.__speed for i in self.__unitVec))

	def setVelocity(self, velocity):

		self.__speed = math.sqrt(sum((i*i for i in velocity)))
		self.__unitVec = tuple((i/self.__speed for i in velocity))

