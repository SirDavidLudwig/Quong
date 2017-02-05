from . import utils
from . client import *
from . server import *
from graphics.screen import *
from scene.game import *
from scene.main_menu import *
from scene.message import *
import pygame
import time

# Custom event type.

SOCKET_EVENT = 0xF0
SOCKET_DISCONNECT = 0xF1
SOCKET_CONNECT = 0xF2
SOCKET_RECIEVE = 0xF3

class Quong():

	def __init__(self, argv):

		utils.quong = self

		self.__client = None
		self.__server = Server(None)

		self.__screen = None
		self.__done = False

		self.__clock = pygame.time.Clock()


	def setScene(self, scene):

		self.__screen.setScene(scene)


	def run(self):

		pygame.init()

		self.__screen = Screen((1024, 576))
		self.__done = False

		self.setScene(MainMenu())

		dt = 0

		while not self.__done:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.__done = True
				elif event.type == SOCKET_CONNECT:
					self.setScene(Game(event.id))
				elif event.type == SOCKET_DISCONNECT:
					self.setScreen(Message(event.message))
				else:
					self.__screen.onEvent(event)

			self.__screen.draw(dt)

			dt = self.__clock.tick(60) / 1000.0

		if self.__client is not None:
			self.__client.stop()

		self.stopServer()

		return 0


	def connect(self, ipAddress, port):

		if self.__client is not None:
			raise Exception("Client connection already established")
			
		self.setScene(Message("Connecting..."))

		self.__client = Client(ipAddress, port)
		self.__client.start()


	def startServer(self, port = 4657):

		self.setScene(Message("Creating game..."))

		if not self.__server.isRunning():
			self.__server.setPort(port)
			self.__server.start()
			self.connect('127.0.0.1', port)

		else:
			raise Exception("ERROR: Server is already running!")


	def stopServer(self):

		self.__server.stop()


	def getClient(self):

		return self.__client


	def getScreen(self):

		return self.__screen


	def getServer(self):

		return self.__server
