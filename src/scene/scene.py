from graphics.frame import Frame
# Scene will keep track of the game and server

class Scene(Frame):

	def __init__(self):

		self.__entities = []

		super(Scene, self).__init__(x=0, y=0, width=100, height=100)


	def draw(self, screen, dt):

		for entity in self.__entities:
			entity.draw(screen, dt)


	def addEntity(self, entity):

		self.__entities.append(entity)


	def onEvent(self, event):

		for entity in self.__entities:
			entity.onEvent(event)
