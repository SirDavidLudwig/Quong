

class Entity():

	def __init__(self):

		self.__x = 0
		self.__y = 0

	# @param
	# dt: Delta Time
	def draw(self, dt):

		pass


	def getX(self):

		return self.__x


	def getY(self):

		return self.__y


	def setX(self, x):

		self.__x = x


	def setY(self, y):

		self.__y = y