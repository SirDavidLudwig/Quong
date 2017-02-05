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


	def start(self):

		self.__thread = Thread(target=self.run)
		self.__thread.start()


	def stop(self):

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



	def disconnect(self):

		pass


	def run(self):

		self.__socket = socket(AF_INET, SOCK_DGRAM)

		if self.connect():
			while self.__running:
				self.receive()

		self.stop()


	def isRunning(self):

		return self.__running