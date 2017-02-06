# The in game scene
from controller.ai_controller import *
from core.client import *
from core.utils import *
import core.quong
from scene.scene import *
from entity.paddle import *
from entity.ball import *
from graphics.frame import *
import pygame


class GameServer(Scene):

	def __init__(self):
		super(GameServer, self).__init__()


	def initialize(self):

		width, height = (1000, 1000)
		ratio = 100 * (height/width)

		self.__gameFrame = Frame((100-ratio)/2, 0, ratio, 100)

		self.addFrame(self.__gameFrame)

		self.__balls = {}
		self.__ball_id = 1

		self.__paddles = []
		self.__paddles.append(Paddle(0, Paddle.LEFT, self.__gameFrame))
		self.__paddles.append(Paddle(1, Paddle.UP, self.__gameFrame))
		self.__paddles.append(Paddle(2, Paddle.RIGHT, self.__gameFrame))
		self.__paddles.append(Paddle(3, Paddle.DOWN, self.__gameFrame))
		for paddle in self.__paddles:
			self.addEntity(paddle)

		self.__controllers = []
		for i in range(4):
			self.__controllers.append(AiController(self.__paddles[i]))


	def onEvent(self, event):

		for controller in self.__controllers:
			controller.onEvent(event)

		super(Game, self).onEvent(event)


	def addBall(self, ball):

		self.__balls[self.__id] = ball
		self.addEntity(ball)


	def removeBall(self, id):

		del self.__balls[id]


	def getController(self, id):

		return self.__controllers[id]


	def getPaddle(self, id):

		return self.__paddles[id]


	def getPaddles(self):

		return self.__paddles


	def setController(self, controller):

		c = self.__controllers[controller.getId()]
		self.__controllers[controller.getId()] = controller
		del c


	def tick(self, screen, dt):

		for controller in self.__controllers:
			controller.tick(screen, dt)

		# Draw scene background and stuff

		# Draw entities last
		super(GameServer, self).draw(screen, dt)
