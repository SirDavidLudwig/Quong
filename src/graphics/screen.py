import pygame


class Screen():

	def __init__(self, resolution = (400, 300)):

		self.__resolution = resolution
		self.__surface = pygame.display.set_mode(resolution)

		self.__clock = pygame.time.Clock()


	def toPixelsX(self, x):

		return x / 100.0 * self.getWidth()


	def toPixelsY(self, y):

		return y / 100.0 * self.getHeight()


	def onEvent(self, event):

		self.__scene.onEvent(event)


	def draw(self, dt):

		self.__surface.fill((0, 0, 0))

		# Draw the scene
		self.__scene.draw(self, dt)

		# Update the screen
		pygame.display.flip()

		# Wait for the next frame
		self.__clock.tick(60)


	def getSurface(self):

		return self.__surface


	def getSize(self):

		return self.__resolution


	def getWidth(self):

		return self.__resolution[0]


	def getHeight(self):

		return self.__resolution[1]


	def getScene(self):

		return self.__scene


	def setScene(self, scene):

		if self.__scene is not None:
			del self.__scene

		self.__scene = scene
