from socket import *
from threading import Thread

class Server():

	def __init__(self, port):

		self.__port = port
		self.__thread = None

		self.__running = False
		self.__clients = None


	def start(self):

		self.__thread = Thread(target=self.run)
		self.__thread.start()


	def stop(self):

		self.__running = False

		self.__socket.close()
		del self.__socket


	def run(self):

		self.__socket = socket(AF_INET, SOCK_DGRAM)
		self.__socket.bind(('', self.__port))
		self.__socket.setblocking(False)

		self.__running = True

		# Main server loop
		while self.__running:
			
			self.connectClients()

			if self.receive():
				self.send()

		self.__socket.close()
		del self.__socket


	def connectClients():

		pass


	def receive(self):

		return False


	def send(self):

		pass


	def isRunning(self):

		return self.__isRunning


	def getPort(self):

		return self.__port


	def setPort(self, port):

		self.__port = port