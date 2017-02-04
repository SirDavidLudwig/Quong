from graphics.screen import *
import pygame
import time


class Quong():

	def __init__(self, argv):

		pass


	def run(self):

		pygame.init()

		self.__screen = Screen()
		self.__done = False

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