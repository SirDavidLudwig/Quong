from entity.button import *
from . scene import *


class MainMenu(Scene):

	def __init__(self):
		super(MainMenu, self).__init__()

		self.__buttonJoin = Button(50, 10, "Join")
		self.__buttonHost = Button(50, 10, "Host")

		self.__buttonJoin.setCenterX(True)
		self.__buttonHost.setCenterX(True)

		self.__buttonJoin.setY(30)
		self.__buttonHost.setY(50)

		self.__buttonJoin.setOnClickListener(self.joinGame)
		self.__buttonHost.setOnClickListener(self.hostGame)

		self.addEntity(self.__buttonJoin)
		self.addEntity(self.__buttonHost)


	def joinGame(self):

		print("You clicked the join button")


	def hostGame(self):

		print("You clicked the host button")


	def draw(self, screen, dt):

		# Draw scene background and stuff

		# Draw entities last
		super(MainMenu, self).draw(screen, dt)


