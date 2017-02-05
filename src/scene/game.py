# The in game scene
from controller.player_controller import *
from core.client import *
from . scene import *
from core.utils import *
from entity.paddle import Paddle
from graphics.debug_frame import DebugFrame
import pygame


class Game(Scene):

	def __init__(self, playerId = 0):
		super(Game, self).__init__()


	def initialize(self):

		width, height = getQuong().getScreen().getRect().size
		ratio = 100 * (height/width)

		self.__gameFrame = DebugFrame((100-ratio)/2, 0, ratio, 100)

		self.addFrame(self.__gameFrame)
		self.addEntity(Paddle(Paddle.LEFT, self.__gameFrame))
		self.addEntity(Paddle(Paddle.UP, self.__gameFrame))
		self.addEntity(Paddle(Paddle.RIGHT, self.__gameFrame))
		self.addEntity(Paddle(Paddle.DOWN, self.__gameFrame))

	
	def onEvent(self, event):

		self.__paddleLeftController.onEvent(event)

		super(Game, self).onEvent(event)


	def draw(self, screen, dt):

		self.__paddleLeftController.tick(screen, dt)

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
