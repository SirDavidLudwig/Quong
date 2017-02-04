from . import utils
from graphics.screen import *
from scene.main_menu import *
import pygame
import time


class Quong():

	def __init__(self, argv):

		utils.quong = self

		self.__screen = None
		self.__done = False


	def setScene(self, scene):

		self.__screen.setScene(scene)


	def run(self):

		pygame.init()

		self.__screen = Screen()
		self.__done = False

		self.setScene(MainMenu())

		dt = time.time()
		
		while not self.__done:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
				else:
					self.__screen.onEvent(event)

			self.__screen.draw(time.time() - dt)
			dt = time.time()

		return 0


	def getScreen(self):

		return self.__screen