from scene.main_menu import *
import pygame


class Screen():

	def __init__(self, resolution = (400, 300)):

		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)
		self.__scene = MainMenu()


	def onEvent(self, event):

		self.__scene.onEvent(event)


	def draw(self, dt):

		# Draw the scene
		self.__scene.draw(self, dt)

		# Update the screen
		pygame.display.flip()


	def getSurface(self):

		return self.__surface


	def getSize(self):

		return self.__resolution
		

	def getWidth(self):

		return self.__resolution[0]


	def getHeight(self):

		return self.__resolution[1]