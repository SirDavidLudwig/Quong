from core.utils import *


class Entity():

	def __init__(self, parent=None):

		if parent is None:
			parent = getQuong().getScreen().getScene()

		self.__x = 0
		self.__y = 0
		self.__parent = parent


	# @param
	# event: pygame event
	def onEvent(self, event):

		pass

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


	def getParent(self):

		return self.__parent

