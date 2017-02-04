

class Frame():

	def __init__(self, x, y, width, height, parent=getQuong().getScreen()):

		self.__entities = []

		self.__x = x
		self.__y = y
		self.__width = width
		self.__height = height

		abs_x = toPixelsX(self.__x, self)
		abs_y = toPixelsY(self.__y, self)
		abs_width = toPixelsX(self.__x+self.__width, self)
		abs_height = toPixelsY(self.__y+self.__height, self)

		self.__rect = pygame.Rect(abs_x, abs_y, abs_width, abs_height)
		self.__parent = parent


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

