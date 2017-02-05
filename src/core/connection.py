import time

class Connection():

	def __init__(self, addr):

		self.__addr = addr
		self.__ping = time.time()


	def getAddress(self):

		return self.__addr