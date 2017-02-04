# The in game scene
from . scene import *


class Game(Scene):

	def __init__(self):
		super(Game, self).__init__()


	def draw(self, screen, dt):

		# Draw scene background and stuff

		# Draw entities last
		super(Game, self).draw(screen, dt)