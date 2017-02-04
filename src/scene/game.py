# The in game scene
from . scene import *
from entity.paddle import Paddle


class Game(Scene):

	def __init__(self):
		super(Game, self).__init__()

		self.addEntity(Paddle(Paddle.LEFT))
		self.addEntity(Paddle(Paddle.UP))
		self.addEntity(Paddle(Paddle.RIGHT))
		self.addEntity(Paddle(Paddle.DOWN))


	def draw(self, screen, dt):

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)
