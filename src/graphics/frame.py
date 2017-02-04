from core.utils import *
import pygame


class Frame():

	def __init__(self, x, y, width, height, parent=None):

		self.__entities = []

		if parent == None:
			parent = getQuong().getScreen()

		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height
		self.__parent = parent

		abs_x = toPixelsX(self.__parent, self.__x)
		abs_y = toPixelsY(self.__parent, self.__y)
		abs_width = toPixelsX(self.__parent, self.__width)
		abs_height = toPixelsY(self.__parent, self.__height)
		print("abs_w", abs_width)

		self.__rect = pygame.Rect(abs_x, abs_y, abs_width, abs_height)


	def draw(self, screen, dt):

		for entity in self.__entities:
			entity.draw(screen, dt)


	def addEntity(self, entity):

		self.__entities.append(entity)


	def onEvent(self, event):

		for entity in self.__entities:
			entity.onEvent(event)


	def getX(self):

		return self.__x

	def getY(self):

		return self.__y


	def getWidth(self):

		return self.__width


	def getHeight(self):

		return self.__height


	def getRect(self):

		return self.__rect


	def getParent(self):

		return self.__parent

