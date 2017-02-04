from socket import *


class Client():

	def __init__(self, ipAddress, port):

		self.__ipAddress = ipAddress
		self.__port = port

		self.__running = False
		self.__socket = None


	def start(self):

		self.__thread = Thread(target=self.run)
		self.__thread.start()


	def stop(self):

		self.disconnect()
		self.__socket.close()
		del self.__socket


	def run(self):

		self.__socket = socket(AF_INET, SOCK_DGRAM)
		self.__socket.connect((self.__ipAddress, self.__port))

		if self.connect():
			while self.__running:
				self.receive()

		self.stop()


	def isRunning(self):

		return self.__running