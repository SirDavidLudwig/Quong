# The in game scene
from controller.network_controller import *
from controller.player_controller import *
from core.client import *
from . scene import *
from core.utils import *
import core.quong
from entity.paddle import *
from entity.ball import *
from graphics.debug_frame import DebugFrame
import pygame


class Game(Scene):

	def __init__(self, playerId = 0):
		super(Game, self).__init__()

		self.__id = playerId


	def initialize(self):

		width, height = getQuong().getScreen().getRect().size
		ratio = 100 * (height/width)

		self.__gameFrame = DebugFrame((100-ratio)/2, 0, ratio, 100)

		self.addFrame(self.__gameFrame)

		self.__paddles = []
		self.__paddles.append(Paddle(0, Paddle.LEFT, self.__gameFrame))
		self.__paddles.append(Paddle(1, Paddle.UP, self.__gameFrame))
		self.__paddles.append(Paddle(2, Paddle.RIGHT, self.__gameFrame))
		self.__paddles.append(Paddle(3, Paddle.DOWN, self.__gameFrame))
		for paddle in self.__paddles:
			self.addEntity(paddle)

		self.__controller = PlayerController(self.__paddles[self.__id])
		self.__paddles[self.__id].loadTexture("../../res/textures/player_paddle.png")

		self.__controllers = [None, None, None, None]
		for i in range(4):
			if i == self.__id:
				self.__controllers[i] = self.__controller
			else:
				self.__controllers[i] = NetworkController(self.__paddles[i])



	def onEvent(self, event):

		for controller in self.__controllers:
			controller.onEvent(event)

		super(Game, self).onEvent(event)


	def draw(self, screen, dt):

		self.__controller.tick(screen, dt)

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
