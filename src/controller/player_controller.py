from . controller import *
import pygame


class PlayerController(Controller):

	def __init__(self, paddle):
		super(PlayerController, self).__init__(paddle)
		

	def onEvent(self, event):

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
				self.setDirection(self.getDirection() | Controller.LEFT_UP)
			elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
				self.setDirection(self.getDirection() | Controller.RIGHT_DOWN)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
				self.setDirection(self.getDirection() & ~Controller.LEFT_UP)
			elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
				self.setDirection(self.getDirection() & ~Controller.RIGHT_DOWN)