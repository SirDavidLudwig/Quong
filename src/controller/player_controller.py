from . controller import *
import core.quong
import pygame
from core.utils import *


class PlayerController(Controller):

	def __init__(self, paddle):
		super(PlayerController, self).__init__(paddle)
		self.__client = getQuong().getClient()


	def onEvent(self, event):

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
				self.setDirection(self.getDirection() | Controller.LEFT_UP)
			elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
				self.setDirection(self.getDirection() | Controller.RIGHT_DOWN)

			self.__client.send({'c':'u', 'd':self.getDirection()})


		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
				self.setDirection(self.getDirection() & ~Controller.LEFT_UP)
			elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
				self.setDirection(self.getDirection() & ~Controller.RIGHT_DOWN)

			self.__client.send({'c':'u', 'd':self.getDirection()})


		elif event.type == core.quong.SOCKET_RECIEVE:
			if event.entity == 'paddle' and event.id == self.getPaddle().getId():
				self.getPaddle().setX(event.x)
				self.getPaddle().setY(event.y)
				print("Setting position")