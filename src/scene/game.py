# The in game scene
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
		self.__paddles.append(Paddle(Paddle.LEFT, self.__gameFrame))
		self.__paddles.append(Paddle(Paddle.UP, self.__gameFrame))
		self.__paddles.append(Paddle(Paddle.RIGHT, self.__gameFrame))
		self.__paddles.append(Paddle(Paddle.DOWN, self.__gameFrame))
		for paddle in self.__paddles:
			self.addEntity(paddle)

		self.__controller = PlayerController(self.__paddles[self.__id])

		self.addEntity(Ball(0.3, self.__gameFrame))
		ball1 = Ball(-0.6, self.__gameFrame)
		ball1.setX(100)
		ball2 = Ball(-1, self.__gameFrame)
		ball2.setY(self.getY() + 100)
		ball3 = Ball(1, self.__gameFrame)
		ball3.setY(self.getY() + 0)
		self.addEntity(ball1)


	def onEvent(self, event):

		self.__controller.onEvent(event)

		super(Game, self).onEvent(event)


	def draw(self, screen, dt):

		self.__controller.tick(screen, dt)

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
