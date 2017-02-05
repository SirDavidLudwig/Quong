from . connection import *
from controller.ai_controller import *
from controller.network_controller import *
import pickle
from socket import *
from threading import Thread

class Server():

	def __init__(self, port):

		self.__port = port
		self.__gameServer = None
		self.__thread = None

		self.__running = False
		self.__clients = None
		self.__queue = []


	def setGameServer(self, gameServer):

		self.__gameServer = gameServer


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

			self.checkTimeout()

			self.receive()

			self.send()

			time.sleep(0.01)
				

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
				self.__clients[i] = Connection(i, addr)
				break

		if id is not None:
			packet = {'c': 'a', 'id': id}
			controller = self.__gameServer.getController(packet['id'])
			self.__gameServer.setController(NetworkController(controller.getPaddle()))
			self.__socket.sendto(self.encodePacket(packet), addr)


	def getConnection(self, address):
		for connection in self.__clients:
			if connection is not None:
				if address == connection.getAddress():
					return connection

		return None


	def checkTimeout(self):

		for i in range(4):
			if self.__clients[i] is not None:
				if time.time() > self.__clients[i].getPing() + 5:
					addr = self.__clients[i].getAddress()
					packet = {'c': 't'}
					self.__socket.sendto(self.encodePacket(packet), addr)
					self.__clients[i] = None


	def receive(self):

		while True:
			try:
				data, addr = self.__socket.recvfrom(1024)

				if self.getConnection(addr) is None:
					self.connectClient(addr, self.decodePacket(data))
					continue

				packet = self.decodePacket(data)

				packetType = packet['c']
				if packetType == 'p':
					self.getConnection(addr).setPing(time.time())

				elif packetType == 'u':
					connection = self.getConnection(addr)
					queuePacket = {
						'entity':'paddle',
						'id':connection.getId(),
						'pos': self.__gameServer.getPaddle(connection.getId()).getPosition(),
						'direction': packet['d']
					}
					self.__queue.append(queuePacket)
					print("Updated")


			except error:
				break

		return False


	def send(self):

		if len(self.__queue) == 0:
			return

		packet = {'c':'u', 'd':self.__queue}

		for connection in self.__clients:
			if connection is not None:
				self.__socket.sendto(self.encodePacket(packet), connection.getAddress())

		for packet in self.__queue:
			if packet['entity'] == 'paddle':
				controller = self.__gameServer.getController(packet['id'])
				controller.setDirection(packet['direction'])

			print(packet['pos'])

		self.__queue = []


	def isRunning(self):

		return self.__running


	def getPort(self):

		return self.__port


	def setPort(self, port):

		self.__port = port