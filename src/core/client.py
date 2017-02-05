import core.quong
import pickle
import pygame
from socket import *
from threading import Thread
import time


class Client():

	def __init__(self, ipAddress, port):

		self.__ipAddress = ipAddress
		self.__port = port

		self.__running = False
		self.__socket = None
		self.__lastPing = time.time()


	def start(self):

		self.__thread = Thread(target=self.run)
		self.__thread.start()


	def stop(self):

		if self.__socket:
			self.disconnect()
			self.__socket.close()
			del self.__socket


	def encodePacket(self, data):
		return pickle.dumps(data)

	
	def decodePacket(self, data):

		return pickle.loads(data)


	def connect(self):

		packet = {'c': 'c'}

		if self.__socket.sendto(self.encodePacket(packet), (self.__ipAddress, self.__port)):

			t = time.time() + 5
			while t > time.time():
				try:
					data, addr = self.__socket.recvfrom(2048)
					break
				except error:
					continue

			print("Received")

			packet = self.decodePacket(data)
			if 'c' in packet and packet['c'] == 'a':
				event = pygame.event.Event(core.quong.SOCKET_CONNECT)
				event.id = packet['id']
				pygame.event.post(event)

				return True

		return False


	def disconnect(self):

		pass


	def run(self):

		self.__socket = socket(AF_INET, SOCK_DGRAM)
		self.__socket.setblocking(False)

		self.__running = True

		if self.connect():
			while self.__running:
				self.ping()
				self.receive()
				time.sleep(0.01)

		self.stop()


	def send(self, data):

		self.__socket.sendto(self.encodePacket(data), (self.__ipAddress, self.__port))


	def receive(self):

		while True:
			try:
				data, addr = self.__socket.recvfrom(2048)
				packet = self.decodePacket(data)
				print(packet)

				if packet['c'] == 't':
					event = pygame.event.Event(core.quong.SOCKET_DISCONNECT)
					event.message = "Timed out"
					pygame.event.post(event)

				elif packet['c'] == 'd':
					event = pygame.event.Event(core.quong.SOCKET_DISCONNECT)
					event.message = "Disconnected"
					pygame.event.post(event)
			except error:
				return


	def ping(self):

		if time.time() > self.__lastPing + 1:
			packet = {'c': 'p'}
			self.__socket.sendto(self.encodePacket(packet), (self.__ipAddress, self.__port))
			self.__lastPing = time.time()


	def isRunning(self):

		return self.__running