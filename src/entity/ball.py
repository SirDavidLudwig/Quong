#ball.py
from . entity import *
import os
import pygame


class Ball(Entity):

	def __init__(self, speed, parent):
		#sedlf.speed_x=.3

		super(Ball, self).__init__(parent)
		self.__speed = speed
		base_path = os.path.dirname(os.path.realpath(__file__)) + "/"
		self.__texture = pygame.image.load(base_path + "../../res/textures/ball.png")
		self.__rect = self.__texture.get_rect()




	def draw(self, screen, dt):

		self.setX(self.getX() + self.__speed * dt)
		self.__rect.left = self.getX ()
		self.__rect.top = self.getY()
		screen.getSurface().blit(self.__texture, self.__rect)
