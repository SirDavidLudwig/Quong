# The in game scene
from . scene import *
from core.utils import *
from entity.paddle import Paddle
from graphics.debug_frame import DebugFrame
import pygame


class Game(Scene):

	def __init__(self):
		super(Game, self).__init__()


	def initialize(self):

		width, height = getQuong().getScreen().getRect().size
		ratio = 100 * (height/width)
		print("r", ratio)

		self.__gameFrame = DebugFrame((100-ratio)/2, 0, ratio, 100)
		print(self.__gameFrame.getRect().size)

		self.addFrame(self.__gameFrame)
		self.addEntity(Paddle(Paddle.LEFT, self.__gameFrame))
		self.addEntity(Paddle(Paddle.UP, self.__gameFrame))
		self.addEntity(Paddle(Paddle.RIGHT, self.__gameFrame))
		self.addEntity(Paddle(Paddle.DOWN, self.__gameFrame))


	def draw(self, screen, dt):

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
