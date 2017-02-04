from . import utils
from . server import *
from graphics.screen import *
from scene.main_menu import *
import pygame
import time


class Quong():

	def __init__(self, argv):

		utils.quong = self

		self.__server = Server(None)

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


	def startServer(self, port = 4657):

		if not self.__server.isRunning():
			self.__server.setPort(port)
			self.__server.start()

		else:
			raise Exception("ERROR: Server is already running!")


	def stopServer(self):

		self.__server.stop()


	def getScreen(self):

		return self.__screen


	def getServer(self):

		return self.__server