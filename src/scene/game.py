# The in game scene
from controller.player_controller import *
from core.client import *
from . scene import *
from entity.paddle import Paddle


class Game(Scene):

	def __init__(self, playerId = 0):
		super(Game, self).__init__()


	def initialize(self):

		self.__paddleLeft = Paddle(Paddle.LEFT)
		self.__paddleUp = Paddle(Paddle.UP)
		self.__paddleRight = Paddle(Paddle.RIGHT)
		self.__paddleDown = Paddle(Paddle.DOWN)

		self.__paddleLeftController = PlayerController(self.__paddleLeft)

		self.addEntity(self.__paddleLeft)
		self.addEntity(self.__paddleUp)
		self.addEntity(self.__paddleRight)
		self.addEntity(self.__paddleDown)


	def onEvent(self, event):

		self.__paddleLeftController.onEvent(event)

		super(Game, self).onEvent(event)


	def draw(self, screen, dt):

		self.__paddleLeftController.tick(screen, dt)

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
