from . connection import *
import pickle
from socket import *
from threading import Thread

class Server():

	def __init__(self, port):

		self.__port = port
		self.__thread = None

		self.__running = False
		self.__clients = None


	def start(self):

		self.__clients = [None, None, None, None]
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

			if self.receive():
				self.send()

		self.__socket.close()
		del self.__socket


	def encodePacket(self, data):
		return pickle.dumps(data)


	def decodePacket(self, packet):
		return pickle.loads(packet)


	def connectClient(self, addr, packet):
		
		id = None

		for i in range(4):
			if self.__clients[i] is None:
				id = i
				self.__clients[i] = Connection(addr)
				break

		if id is not None:
			packet = {'c': 'a', 'id': id}
			self.__socket.sendto(self.encodePacket(packet), addr)


	def receive(self):

		while True:
			try:
				data, addr = self.__socket.recvfrom(1024)

				if addr not in self.__clients:
					self.connectClient(addr, self.decodePacket(data))

			except error:
				break

		return False


	def send(self):

		pass  


	def isRunning(self):

		return self.__running


	def getPort(self):

		return self.__port


	def setPort(self, port):

		self.__port = port