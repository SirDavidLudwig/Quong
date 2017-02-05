import time

class Connection():

	def __init__(self, id, addr):

		self.__id = id
		self.__addr = addr
		self.__ping = time.time()


	def getId(self):

		return self.__id


	def getAddress(self):

		return self.__addr


	def getPing(self):

		return self.__ping


	def setPing(self, ping):
		self.__ping = ping