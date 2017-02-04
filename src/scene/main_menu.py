from entity.paddle import *
from . scene import *


class MainMenu(Scene):

	def __init__(self):
		super(MainMenu, self).__init__()

		paddle = Paddle()

		self.addEntity(paddle)


	def onEvent(self, event):

		pass


